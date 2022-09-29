import getfem as gf
import numpy as np
import pyvista as pv

pv.set_plot_theme("document")


mesh = gf.Mesh("empty", 2)
gt = gf.GeoTrans("GT_PK(2,2)")
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
    2.14765692,
    2.23862171,
    2.25020337,
    1.86968768,
    1.87159467,
    1.96065235,
    2.03794599,
    2.17339182,
    2.27764177,
    2.31274986,
    2.39741039,
    1.98434079,
    2.07305408,
    2.10424995,
    1.21609759,
    0.956094027,
    0.928863049,
    0.61776185,
    0.889270782,
    1.31829286,
    1.04687166,
    1.00719166,
    0.672223806,
    0.322496414,
    0.322496414,
    0.0,
    0.298612624,
    0.353529572,
    0.349727362,
    0.0,
    2.65699625,
    2.81134081,
    3.01119447,
    2.61071682,
    2.94083118,
    2.30545712,
    2.43494749,
    2.53958321,
    2.9951036,
    3.22274947,
    2.78685355,
    3.04174995,
    2.5862298,
    2.62524986,
    1.67959762,
    1.97057164,
    2.08827782,
    1.82472491,
    2.21910143,
    1.47279274,
    1.72132254,
    1.58562696,
    1.92740786,
    2.45301008,
    2.61824918,
    2.27724075,
    2.13139391,
    1.97093856,
    1.13782501,
    1.19301391,
    0.754643679,
    1.29641628,
    1.36630476,
    0.865021467,
    0.404916286,
    0.404916286,
    0.0,
    0.460105181,
    0.464885771,
    0.0,
    1.45229125,
    1.52437818,
    1.70947433,
    1.33727348,
    1.40119362,
    1.56530046,
    1.79687095,
    1.88353753,
    1.65181267,
    1.72478402,
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
    0.49989599,
    0.361214399,
    0.577865005,
    0.526890993,
    0.352538496,
    0.388209403,
    0.285623163,
    0.161709383,
    0.161709383,
    0.0,
    0.201135173,
    0.124891631,
    0.12391378,
    0.0,
    0.935727477,
    1.14698243,
    1.00701976,
    1.09537792,
    0.89571166,
    1.18152106,
    1.42680883,
    1.2698791,
    1.37530303,
    1.26342022,
    1.1176703,
    1.14575005,
    0.988790989,
    1.56597483,
    1.40338278,
    1.43725002,
    1.19814098,
    0.876531482,
    1.03466594,
    0.800088763,
    0.628338218,
    0.898422956,
    0.650229692,
    0.475452751,
    0.27594775,
    0.355370194,
    0.27594775,
    0.0,
    0.199505001,
    0.0,
    2.05050874,
    1.84404683,
    2.10717726,
    1.63991952,
    1.68215442,
    1.55311477,
    1.39122248,
    1.19474387,
    1.27389979,
    1.41301358,
    1.62920785,
    1.26315451,
    1.05902719,
    0.91628772,
    1.6585387,
    1.93908858,
    1.79581547,
    2.18778563,
    2.49518013,
    2.356915,
    1.82968259,
    2.12143278,
    1.87475002,
    2.40198231,
    2.7217207,
    2.45825005,
    0.963071585,
    1.06419837,
    0.968645692,
    0.743589222,
    0.840174794,
    0.766392231,
    0.734150469,
    0.808041453,
    0.563807368,
    0.633023739,
]
mesh.add_convex(
    gt,
    [
        [x[29], x[38], x[15], x[36], x[37], x[12]],
        [y[29], y[38], y[15], y[36], y[37], y[12]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[0], x[35], x[12], x[39], x[37], x[15]],
        [y[0], y[35], y[12], y[39], y[37], y[15]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[13], x[43], x[29], x[41], x[42], x[1]],
        [y[13], y[43], y[29], y[41], y[42], y[1]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[12], x[40], x[1], x[36], x[42], x[29]],
        [y[12], y[40], y[1], y[36], y[42], y[29]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[14], x[46], x[3], x[44], x[45], x[29]],
        [y[14], y[46], y[3], y[44], y[45], y[29]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[15], x[38], x[29], x[47], x[45], x[3]],
        [y[15], y[38], y[29], y[47], y[45], y[3]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[2], x[50], x[14], x[48], x[49], x[13]],
        [y[2], y[50], y[14], y[48], y[49], y[13]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[29], x[43], x[13], x[44], x[49], x[14]],
        [y[29], y[43], y[13], y[44], y[49], y[14]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[30], x[54], x[19], x[52], x[53], x[16]],
        [y[30], y[54], y[19], y[52], y[53], y[16]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[4], x[51], x[16], x[55], x[53], x[19]],
        [y[4], y[51], y[16], y[55], y[53], y[19]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[17], x[59], x[30], x[57], x[58], x[5]],
        [y[17], y[59], y[30], y[57], y[58], y[5]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[16], x[56], x[5], x[52], x[58], x[30]],
        [y[16], y[56], y[5], y[52], y[58], y[30]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[18], x[62], x[7], x[60], x[61], x[30]],
        [y[18], y[62], y[7], y[60], y[61], y[30]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[19], x[54], x[30], x[63], x[61], x[7]],
        [y[19], y[54], y[30], y[63], y[61], y[7]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[6], x[66], x[18], x[64], x[65], x[17]],
        [y[6], y[66], y[18], y[64], y[65], y[17]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[30], x[59], x[17], x[60], x[65], x[18]],
        [y[30], y[59], y[17], y[60], y[65], y[18]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[8], x[67], x[20], x[69], x[68], x[22]],
        [y[8], y[67], y[20], y[69], y[68], y[22]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[20], x[70], x[31], x[68], x[71], x[22]],
        [y[20], y[70], y[31], y[68], y[71], y[22]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[20], x[72], x[0], x[70], x[73], x[31]],
        [y[20], y[72], y[0], y[70], y[73], y[31]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[0], x[39], x[15], x[73], x[74], x[31]],
        [y[0], y[39], y[15], y[73], y[74], y[31]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[22], x[71], x[31], x[76], x[75], x[9]],
        [y[22], y[71], y[31], y[76], y[75], y[9]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[31], x[77], x[21], x[75], x[78], x[9]],
        [y[31], y[77], y[21], y[75], y[78], y[9]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[31], x[74], x[15], x[77], x[79], x[21]],
        [y[31], y[74], y[15], y[77], y[79], y[21]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[15], x[47], x[3], x[79], x[80], x[21]],
        [y[15], y[47], y[3], y[79], y[80], y[21]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[10], x[81], x[23], x[83], x[82], x[25]],
        [y[10], y[81], y[23], y[83], y[82], y[25]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[23], x[84], x[32], x[82], x[85], x[25]],
        [y[23], y[84], y[32], y[82], y[85], y[25]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[23], x[86], x[5], x[84], x[87], x[32]],
        [y[23], y[86], y[5], y[84], y[87], y[32]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[5], x[88], x[24], x[87], x[89], x[32]],
        [y[5], y[88], y[24], y[87], y[89], y[32]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[25], x[85], x[32], x[91], x[90], x[8]],
        [y[25], y[85], y[32], y[91], y[90], y[8]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[32], x[92], x[20], x[90], x[67], x[8]],
        [y[32], y[92], y[20], y[90], y[67], y[8]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[32], x[89], x[24], x[92], x[93], x[20]],
        [y[32], y[89], y[24], y[92], y[93], y[20]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[24], x[94], x[0], x[93], x[72], x[20]],
        [y[24], y[94], y[0], y[93], y[72], y[20]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[5], x[86], x[23], x[57], x[95], x[17]],
        [y[5], y[86], y[23], y[57], y[95], y[17]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[23], x[96], x[33], x[95], x[97], x[17]],
        [y[23], y[96], y[33], y[95], y[97], y[17]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[23], x[81], x[10], x[96], x[98], x[33]],
        [y[23], y[81], y[10], y[96], y[98], y[33]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[10], x[99], x[26], x[98], x[100], x[33]],
        [y[10], y[99], y[26], y[98], y[100], y[33]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[17], x[97], x[33], x[64], x[101], x[6]],
        [y[17], y[97], y[33], y[64], y[101], y[6]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[33], x[102], x[27], x[101], x[103], x[6]],
        [y[33], y[102], y[27], y[101], y[103], y[6]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[33], x[100], x[26], x[102], x[104], x[27]],
        [y[33], y[100], y[26], y[102], y[104], y[27]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[26], x[105], x[11], x[104], x[106], x[27]],
        [y[26], y[105], y[11], y[104], y[106], y[27]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[34], x[109], x[24], x[107], x[108], x[16]],
        [y[34], y[109], y[24], y[107], y[108], y[16]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[5], x[56], x[16], x[88], x[108], x[24]],
        [y[5], y[56], y[16], y[88], y[108], y[24]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[28], x[112], x[34], x[110], x[111], x[4]],
        [y[28], y[112], y[34], y[110], y[111], y[4]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[16], x[51], x[4], x[107], x[111], x[34]],
        [y[16], y[51], y[4], y[107], y[111], y[34]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[12], x[35], x[0], x[113], x[114], x[34]],
        [y[12], y[35], y[0], y[113], y[114], y[34]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[24], x[109], x[34], x[94], x[114], x[0]],
        [y[24], y[109], y[34], y[94], y[114], y[0]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[1], x[40], x[12], x[115], x[116], x[28]],
        [y[1], y[40], y[12], y[115], y[116], y[28]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[34], x[112], x[28], x[113], x[116], x[12]],
        [y[34], y[112], y[28], y[113], y[116], y[12]],
    ],
)

mesh.save("fine-triangle-2d.msh")
mesh.export_to_vtk("fine-triangle-2d.vtk", "ascii")

mesh = pv.read("fine-triangle-2d.vtk")

plotter = pv.Plotter()
plotter.add_mesh(mesh)
plotter.add_mesh(
    mesh.separate_cells().extract_feature_edges(),
    show_edges=True,
    line_width=3,
    color="black",
)
plotter.add_points(
    mesh.points, render_points_as_spheres=True, point_size=10.0, color="red"
)
plotter.show(cpos="xy", screenshot="fine-triangle-2d.png")