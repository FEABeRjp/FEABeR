import getfem as gf

mesh = gf.Mesh("load", "./mesh/coarse-quadrilateron-1d.msh")
elements_degree = 1

mfu = gf.MeshFem(mesh, 2)
mfu.set_classical_fem(elements_degree)

mim = gf.MeshIm(mesh, elements_degree * 2)

md = gf.Model("real")
md.add_fem_variable("u", mfu)
