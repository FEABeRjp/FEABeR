import getfem as gf
import numpy as np
import pyvista as pv

pv.set_plot_theme("document")

mesh = gf.Mesh("empty", 2)
gt = gf.GeoTrans("GT_Q2_INCOMPLETE(2)")
x = [
    2.12968779,
    1.78302097,
    2.0,
    2.41700006,
    1.16499996,
    1.36939037,
    0.0,
    0.0,
    2.83276558,
    3.25,
    1.78299999,
    0.0,
    1.95635438,
    1.93760836,
    2.20849991,
    2.33895946,
    1.26719522,
    0.699454725,
    0.0,
    0.590530932,
    2.48122668,
    2.83349991,
    3.14145494,
    1.57619524,
    1.78156114,
    2.36494803,
    0.920210361,
    0.0,
    1.49321365,
    2.13828373,
    0.644992828,
    2.7402072,
    2.07325459,
    0.809832573,
    1.63738739,
    2.04302096,
    2.04731894,
    2.23862171,
    2.25020337,
    1.86968768,
    1.87159467,
    2.03794599,
    2.17339182,
    2.31274986,
    2.39741039,
    1.98434079,
    2.10424995,
    1.21609759,
    0.956094027,
    0.61776185,
    0.889270782,
    1.31829286,
    1.04687166,
    0.672223806,
    0.322496414,
    0.0,
    0.298612624,
    0.353529572,
    0.0,
    2.65699625,
    2.61071682,
    2.94083118,
    3.01119447,
    2.30545712,
    2.53958321,
    2.78685355,
    3.04174995,
    3.22274947,
    2.62524986,
    1.67959762,
    1.82472491,
    2.21910143,
    2.08827782,
    1.47279274,
    1.58562696,
    1.92740786,
    2.27724075,
    2.61824918,
    1.97093856,
    1.19301391,
    0.754643679,
    1.36630476,
    0.865021467,
    0.404916286,
    0.0,
    0.464885771,
    0.0,
    1.45229125,
    1.70947433,
    1.33727348,
    1.56530046,
    1.79687095,
    1.65181267,
]
y = [
    0.748563945,
    0.453000009,
    0.0,
    0.0,
    0.812830687,
    1.30441773,
    1.58299994,
    1.0,
    1.34800005,
    0.0,
    2.29920578,
    2.75,
    0.600781977,
    0.24782756,
    0.0,
    0.399010003,
    1.05862427,
    1.51526558,
    1.29149997,
    0.955415249,
    1.04828203,
    0.0,
    0.704780996,
    1.80181181,
    1.06977248,
    1.88628185,
    2.63746476,
    2.16650009,
    0.66526556,
    0.323418766,
    1.23534048,
    0.551895499,
    1.47802711,
    2.07636523,
    0.867518961,
    0.674672961,
    0.462100387,
    0.361214399,
    0.577865005,
    0.526890993,
    0.352538496,
    0.285623163,
    0.161709383,
    0.0,
    0.201135173,
    0.124891631,
    0.0,
    0.935727477,
    1.14698243,
    1.09537792,
    0.89571166,
    1.18152106,
    1.42680883,
    1.37530303,
    1.26342022,
    1.14575005,
    0.988790989,
    1.56597483,
    1.43725002,
    1.19814098,
    0.800088763,
    0.628338218,
    1.03466594,
    0.898422956,
    0.475452751,
    0.27594775,
    0.0,
    0.355370194,
    0.0,
    2.05050874,
    1.63991952,
    1.68215442,
    2.10717726,
    1.55311477,
    1.19474387,
    1.27389979,
    1.26315451,
    1.62920785,
    0.91628772,
    1.93908858,
    1.79581547,
    2.49518013,
    2.356915,
    2.12143278,
    1.87475002,
    2.7217207,
    2.45825005,
    0.963071585,
    0.968645692,
    0.743589222,
    0.766392231,
    0.734150469,
    0.563807368,
]
mesh.add_convex(
    gt,
    [
        [x[0], x[35], x[12], x[38], x[36], x[15], x[37], x[29]],
        [y[0], y[35], y[12], y[38], y[36], y[15], y[37], y[29]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[12], x[39], x[1], x[36], x[40], x[29], x[41], x[13]],
        [y[12], y[39], y[1], y[36], y[40], y[29], y[41], y[13]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[15], x[37], x[29], x[44], x[42], x[3], x[43], x[14]],
        [y[15], y[37], y[29], y[44], y[42], y[3], y[43], y[14]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[29], x[41], x[13], x[42], x[45], x[14], x[46], x[2]],
        [y[29], y[41], y[13], y[42], y[45], y[14], y[46], y[2]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[4], x[47], x[16], x[50], x[48], x[19], x[49], x[30]],
        [y[4], y[47], y[16], y[50], y[48], y[19], y[49], y[30]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[16], x[51], x[5], x[48], x[52], x[30], x[53], x[17]],
        [y[16], y[51], y[5], y[48], y[52], y[30], y[53], y[17]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[19], x[49], x[30], x[56], x[54], x[7], x[55], x[18]],
        [y[19], y[49], y[30], y[56], y[54], y[7], y[55], y[18]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[30], x[53], x[17], x[54], x[57], x[18], x[58], x[6]],
        [y[30], y[53], y[17], y[54], y[57], y[18], y[58], y[6]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[8], x[59], x[20], x[62], x[60], x[22], x[61], x[31]],
        [y[8], y[59], y[20], y[62], y[60], y[22], y[61], y[31]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[20], x[63], x[0], x[60], x[38], x[31], x[64], x[15]],
        [y[20], y[63], y[0], y[60], y[38], y[31], y[64], y[15]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[22], x[61], x[31], x[67], x[65], x[9], x[66], x[21]],
        [y[22], y[61], y[31], y[67], y[65], y[9], y[66], y[21]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[31], x[64], x[15], x[65], x[44], x[21], x[68], x[3]],
        [y[31], y[64], y[15], y[65], y[44], y[21], y[68], y[3]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[10], x[69], x[23], x[72], x[70], x[25], x[71], x[32]],
        [y[10], y[69], y[23], y[72], y[70], y[25], y[71], y[32]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[23], x[73], x[5], x[70], x[74], x[32], x[75], x[24]],
        [y[23], y[73], y[5], y[70], y[74], y[32], y[75], y[24]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[25], x[71], x[32], x[77], x[76], x[8], x[59], x[20]],
        [y[25], y[71], y[32], y[77], y[76], y[8], y[59], y[20]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[32], x[75], x[24], x[76], x[78], x[20], x[63], x[0]],
        [y[32], y[75], y[24], y[76], y[78], y[20], y[63], y[0]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[5], x[73], x[23], x[52], x[79], x[17], x[80], x[33]],
        [y[5], y[73], y[23], y[52], y[79], y[17], y[80], y[33]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[23], x[69], x[10], x[79], x[81], x[33], x[82], x[26]],
        [y[23], y[69], y[10], y[79], y[81], y[33], y[82], y[26]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[17], x[80], x[33], x[57], x[83], x[6], x[84], x[27]],
        [y[17], y[80], y[33], y[57], y[83], y[6], y[84], y[27]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[33], x[82], x[26], x[83], x[85], x[27], x[86], x[11]],
        [y[33], y[82], y[26], y[83], y[85], y[27], y[86], y[11]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[5], x[51], x[16], x[74], x[87], x[24], x[88], x[34]],
        [y[5], y[51], y[16], y[74], y[87], y[24], y[88], y[34]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[16], x[47], x[4], x[87], x[89], x[34], x[90], x[28]],
        [y[16], y[47], y[4], y[87], y[89], y[34], y[90], y[28]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[24], x[88], x[34], x[78], x[91], x[0], x[35], x[12]],
        [y[24], y[88], y[34], y[78], y[91], y[0], y[35], y[12]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[34], x[90], x[28], x[91], x[92], x[12], x[39], x[1]],
        [y[34], y[90], y[28], y[91], y[92], y[12], y[39], y[1]],
    ],
)
mesh.save("fine-quadrilateron-2d.msh")
mesh.export_to_vtk("fine-quadrilateron-2d.vtk", "ascii")

mesh = pv.read("fine-quadrilateron-2d.vtk")

plotter = pv.Plotter()
plotter.add_mesh(mesh)
plotter.add_mesh(
    mesh.separate_cells().extract_feature_edges(),
    show_edges=True,
    line_width=3,
    color="black",
)
plotter.show(cpos="xy", screenshot="fine-quadrilateron-2d.png")
