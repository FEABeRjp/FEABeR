###############################################################################

import numpy as np
import getfem as gf

try:
    import pyvista as pv

    pv.set_plot_theme("document")
except:
    print("\n\n** Could not load pyvista. Did you install it ?\n")
    print("   ( https://docs.pyvista.org/getting-started/installation.html ) **\n\n")
    sys.exit()

###############################################################################

E = 1.0  # Young Modulus
nus = [0.0, 0.2, 0.3, 0.4, 0.5]  # Poisson ratio
elements_degree = 2  # Degree of the finite element methods
F = 1.00 / 1.0  # Force density at the right boundary

###############################################################################

mesh = gf.Mesh(
    "cartesian", np.linspace(0.0, 4.0, 40 + 1), np.linspace(0.0, 1.0, 10 + 1)
)

###############################################################################

P = mesh.pts()
ccenter = abs(P[1, :] - 0.5) < 1e-6
pcenter = np.compress(ccenter, list(range(0, mesh.nbpts())))

fb1 = mesh.outer_faces_with_direction([1.0, 0.0], 0.01)
fb2 = mesh.outer_faces_with_direction([-1.0, 0.0], 0.01)
fb3 = mesh.faces_from_pid(pcenter)

RIGHT_BOUND = 1
LEFT_BOUND = 2
CENTER_AXIS = 3

mesh.set_region(RIGHT_BOUND, fb1)
mesh.set_region(LEFT_BOUND, fb2)
mesh.set_region(CENTER_AXIS, fb3)

###############################################################################

mesh.export_to_vtk("mesh.vtk", "ascii")

m = pv.read("mesh.vtk")
m.plot(show_edges="True", cpos="xy")

###############################################################################

mfu = gf.MeshFem(mesh, 2)
mfu.set_classical_fem(elements_degree)
mim = gf.MeshIm(mesh, elements_degree * 2)

###############################################################################

mds = []
for nu in nus:
    md = gf.Model("real")
    md.add_fem_variable("u", mfu)
    md.add_initialized_data("E", [E])
    md.add_initialized_data("nu", [nu])
    md.add_initialized_data("F", [F, 0.0])
    md.add_isotropic_linearized_elasticity_pstress_brick(mim, "u", "E", "nu")
    md.add_source_term_brick(mim, "u", "F", RIGHT_BOUND)
    md.add_initialized_data("r2", [0.0, 0.0])
    md.add_initialized_data("H2", [[1.0, 0.0], [0.0, 0.0]])
    md.add_initialized_data("r3", [0.0, 0.0])
    md.add_initialized_data("H3", [[0.0, 0.0], [0.0, 1.0]])
    md.add_generalized_Dirichlet_condition_with_multipliers(
        mim,
        "u",
        mfu,
        LEFT_BOUND,
        "r2",
        "H2",
    )
    md.add_generalized_Dirichlet_condition_with_multipliers(
        mim,
        "u",
        mfu,
        CENTER_AXIS,
        "r3",
        "H3",
    )
    md.add_source_term_brick(mim, "u", "F", LEFT_BOUND)
    mds.append(md)

###############################################################################

for md in mds:
    md.solve()

###############################################################################

U0 = mds[0].variable("u")
U1 = mds[1].variable("u")
U2 = mds[2].variable("u")
U3 = mds[3].variable("u")
U4 = mds[4].variable("u")

###############################################################################

mfu.export_to_vtk("displacement0.vtk", "ascii", mfu, U0, "Displacements")
mfu.export_to_vtk("displacement1.vtk", "ascii", mfu, U1, "Displacements")
mfu.export_to_vtk("displacement2.vtk", "ascii", mfu, U2, "Displacements")
mfu.export_to_vtk("displacement3.vtk", "ascii", mfu, U3, "Displacements")
mfu.export_to_vtk("displacement4.vtk", "ascii", mfu, U4, "Displacements")

###############################################################################

d0 = pv.read("displacement0.vtk")
d1 = pv.read("displacement1.vtk")
d2 = pv.read("displacement2.vtk")
d3 = pv.read("displacement3.vtk")
d4 = pv.read("displacement4.vtk")

p = pv.Plotter(shape=(5, 1))
p.open_gif("Displacements.gif")
p.subplot(0, 0)
p.add_text("Poission's ratio = " + str(nus[0]), position="left_edge", font_size=9)
actor01 = p.add_mesh(d0.extract_feature_edges(), line_width=2, color="black")
p.camera_position = "xy"
p.camera.zoom(1.0)
p.subplot(1, 0)
p.add_text("Poission's ratio = " + str(nus[1]), position="left_edge", font_size=9)
actor11 = p.add_mesh(d1.extract_feature_edges(), line_width=2, color="black")
p.camera_position = "xy"
p.camera.zoom(1.0)
p.subplot(2, 0)
p.add_text("Poission's ratio = " + str(nus[2]), position="left_edge", font_size=9)
actor21 = p.add_mesh(d2.extract_feature_edges(), line_width=2, color="black")
p.camera_position = "xy"
p.camera.zoom(1.0)
p.subplot(3, 0)
p.add_text("Poission's ratio = " + str(nus[3]), position="left_edge", font_size=9)
actor31 = p.add_mesh(d3.extract_feature_edges(), line_width=2, color="black")
p.camera_position = "xy"
p.camera.zoom(1.0)
p.subplot(4, 0)
p.add_text("Poission's ratio = " + str(nus[4]), position="left_edge", font_size=9)
actor41 = p.add_mesh(d4.extract_feature_edges(), line_width=2, color="black")
p.camera_position = "xy"
p.camera.zoom(1.0)
p.remove_actor(actor01)
p.remove_actor(actor11)
p.remove_actor(actor21)
p.remove_actor(actor31)
p.remove_actor(actor41)

for factor in np.linspace(0.0, 1.0, 5):
    p.subplot(0, 0)
    actor00 = p.add_mesh(
        d0.warp_by_vector(factor=factor),
        line_width=2,
        scalars="Displacements",
        component=1,
    )
    actor01 = p.add_mesh(d0.extract_feature_edges(), line_width=2, color="black")
    p.subplot(1, 0)
    actor10 = p.add_mesh(
        d1.warp_by_vector(factor=factor),
        line_width=2,
        scalars="Displacements",
        component=1,
    )
    actor11 = p.add_mesh(d1.extract_feature_edges(), line_width=2, color="black")
    p.subplot(2, 0)
    actor20 = p.add_mesh(
        d2.warp_by_vector(factor=factor),
        line_width=2,
        scalars="Displacements",
        component=1,
    )
    actor21 = p.add_mesh(d2.extract_feature_edges(), line_width=2, color="black")
    p.subplot(3, 0)
    actor30 = p.add_mesh(
        d3.warp_by_vector(factor=factor),
        line_width=2,
        scalars="Displacements",
        component=1,
    )
    actor31 = p.add_mesh(d3.extract_feature_edges(), line_width=2, color="black")
    p.subplot(4, 0)
    actor40 = p.add_mesh(
        d4.warp_by_vector(factor=factor),
        line_width=2,
        scalars="Displacements",
        component=1,
    )
    actor41 = p.add_mesh(d4.extract_feature_edges(), line_width=2, color="black")
    p.remove_scalar_bar()
    p.render()
    p.write_frame()
    p.remove_actor(actor00)
    p.remove_actor(actor01)
    p.remove_actor(actor10)
    p.remove_actor(actor11)
    p.remove_actor(actor20)
    p.remove_actor(actor21)
    p.remove_actor(actor30)
    p.remove_actor(actor31)
    p.remove_actor(actor40)
    p.remove_actor(actor41)
p.close()
