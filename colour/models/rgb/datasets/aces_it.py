# -*- coding: utf-8 -*-
"""
Academy Color Encoding System - Input Transform Dataset
=======================================================

Defines the *Academy Color Encoding System* (ACES) *Input Transform* datasets.

See Also
--------
`RGB Colourspaces Jupyter Notebook
<http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/\
blob/master/notebooks/models/rgb.ipynb>`_

References
----------
-   :cite:`TheAcademyofMotionPictureArtsandSciences2014q` : The Academy of
    Motion Picture Arts and Sciences, Science and Technology Council, & Academy
    Color Encoding System (ACES) Project Subcommittee. (2014). Technical
    Bulletin TB-2014-004 - Informative Notes on SMPTE ST 2065-1 - Academy Color
    Encoding Specification (ACES). Retrieved from
    https://github.com/ampas/aces-dev/tree/master/documents
-   :cite:`TheAcademyofMotionPictureArtsandSciences2014r` : The Academy of
    Motion Picture Arts and Sciences, Science and Technology Council, & Academy
    Color Encoding System (ACES) Project Subcommittee. (2014). Technical
    Bulletin TB-2014-012 - Academy Color Encoding System Version 1.0 Component
    Names. Retrieved from
    https://github.com/ampas/aces-dev/tree/master/documents
-   :cite:`TheAcademyofMotionPictureArtsandSciencese` : The Academy of Motion
    Picture Arts and Sciences, Science and Technology Council, & Academy Color
    Encoding System (ACES) Project Subcommittee. (n.d.). Academy Color Encoding
    System. Retrieved February 24, 2014, from
    http://www.oscars.org/science-technology/council/projects/aces.html
"""

from __future__ import division, unicode_literals

from colour.characterisation import RGB_SpectralSensitivities

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['ACES_RICD_DATA', 'ACES_RICD']

ACES_RICD_DATA = {
    360.0: (1.20e-06, 0.0000000, 5.70e-06),
    361.0: (1.40e-06, 0.0000000, 6.40e-06),
    362.0: (1.50e-06, 0.0000000, 7.20e-06),
    363.0: (1.70e-06, 0.0000000, 8.00e-06),
    364.0: (1.90e-06, 0.0000000, 9.00e-06),
    365.0: (2.20e-06, 0.0000000, 1.02e-05),
    366.0: (2.40e-06, 0.0000000, 1.14e-05),
    367.0: (2.70e-06, 0.0000000, 1.28e-05),
    368.0: (3.10e-06, 0.0000000, 1.44e-05),
    369.0: (3.50e-06, 0.0000000, 1.62e-05),
    370.0: (3.90e-06, 0.0000000, 1.82e-05),
    371.0: (4.30e-06, 0.0000000, 2.04e-05),
    372.0: (4.90e-06, 0.0000000, 2.28e-05),
    373.0: (5.40e-06, 0.0000000, 2.56e-05),
    374.0: (6.10e-06, 0.0000000, 2.88e-05),
    375.0: (6.90e-06, 0.0000000, 3.26e-05),
    376.0: (7.90e-06, 1.00e-07, 3.72e-05),
    377.0: (9.00e-06, 1.00e-07, 4.25e-05),
    378.0: (1.02e-05, 1.00e-07, 4.83e-05),
    379.0: (1.15e-05, 1.00e-07, 5.43e-05),
    380.0: (1.28e-05, 1.00e-07, 6.03e-05),
    381.0: (1.41e-05, 1.00e-07, 6.63e-05),
    382.0: (1.54e-05, 1.00e-07, 7.25e-05),
    383.0: (1.69e-05, 1.00e-07, 7.95e-05),
    384.0: (1.87e-05, 1.00e-07, 8.81e-05),
    385.0: (2.09e-05, 1.00e-07, 9.87e-05),
    386.0: (2.37e-05, 2.00e-07, 0.0001119),
    387.0: (2.71e-05, 2.00e-07, 0.0001278),
    388.0: (3.09e-05, 2.00e-07, 0.0001458),
    389.0: (3.51e-05, 3.00e-07, 0.0001659),
    390.0: (3.97e-05, 3.00e-07, 0.0001876),
    391.0: (4.45e-05, 3.00e-07, 0.0002106),
    392.0: (4.99e-05, 4.00e-07, 0.0002358),
    393.0: (5.59e-05, 5.00e-07, 0.0002646),
    394.0: (6.31e-05, 5.00e-07, 0.0002984),
    395.0: (7.16e-05, 6.00e-07, 0.0003388),
    396.0: (8.19e-05, 7.00e-07, 0.0003877),
    397.0: (9.38e-05, 8.00e-07, 0.0004444),
    398.0: (0.0001068, 9.00e-07, 0.0005063),
    399.0: (0.0001204, 1.00e-06, 0.0005706),
    400.0: (0.0001339, 1.10e-06, 0.0006348),
    401.0: (0.0001469, 1.20e-06, 0.0006968),
    402.0: (0.0001604, 1.30e-06, 0.0007612),
    403.0: (0.0001757, 1.50e-06, 0.0008341),
    404.0: (0.0001941, 1.70e-06, 0.0009219),
    405.0: (0.0002169, 2.00e-06, 0.0010309),
    406.0: (0.0002452, 2.30e-06, 0.0011658),
    407.0: (0.0002786, 2.70e-06, 0.0013256),
    408.0: (0.0003169, 3.20e-06, 0.0015090),
    409.0: (0.0003598, 3.80e-06, 0.0017144),
    410.0: (0.0004070, 4.40e-06, 0.0019403),
    411.0: (0.0004583, 5.10e-06, 0.0021862),
    412.0: (0.0005147, 5.90e-06, 0.0024568),
    413.0: (0.0005773, 6.90e-06, 0.0027577),
    414.0: (0.0006474, 8.00e-06, 0.0030947),
    415.0: (0.0007262, 9.30e-06, 0.0034736),
    416.0: (0.0008134, 1.09e-05, 0.0038937),
    417.0: (0.0009090, 1.28e-05, 0.0043545),
    418.0: (0.0010141, 1.51e-05, 0.0048619),
    419.0: (0.0011297, 1.81e-05, 0.0054216),
    420.0: (0.0012570, 2.18e-05, 0.0060397),
    421.0: (0.0013971, 2.65e-05, 0.0067216),
    422.0: (0.0015472, 3.20e-05, 0.0074534),
    423.0: (0.0017023, 3.84e-05, 0.0082124),
    424.0: (0.0018579, 4.56e-05, 0.0089758),
    425.0: (0.0020090, 5.37e-05, 0.0097205),
    426.0: (0.0021532, 6.26e-05, 0.0104345),
    427.0: (0.0022907, 7.25e-05, 0.0111186),
    428.0: (0.0024207, 8.33e-05, 0.0117700),
    429.0: (0.0025425, 9.51e-05, 0.0123856),
    430.0: (0.0026557, 0.0001081, 0.0129626),
    431.0: (0.0027590, 0.0001221, 0.0134962),
    432.0: (0.0028521, 0.0001372, 0.0139842),
    433.0: (0.0029352, 0.0001534, 0.0144275),
    434.0: (0.0030087, 0.0001705, 0.0148269),
    435.0: (0.0030728, 0.0001886, 0.0151831),
    436.0: (0.0031276, 0.0002077, 0.0154960),
    437.0: (0.0031730, 0.0002277, 0.0157663),
    438.0: (0.0032096, 0.0002486, 0.0159962),
    439.0: (0.0032377, 0.0002702, 0.0161881),
    440.0: (0.0032578, 0.0002926, 0.0163441),
    441.0: (0.0032702, 0.0003156, 0.0164656),
    442.0: (0.0032753, 0.0003394, 0.0165552),
    443.0: (0.0032740, 0.0003640, 0.0166173),
    444.0: (0.0032672, 0.0003897, 0.0166563),
    445.0: (0.0032557, 0.0004167, 0.0166766),
    446.0: (0.0032400, 0.0004450, 0.0166801),
    447.0: (0.0032202, 0.0004745, 0.0166682),
    448.0: (0.0031972, 0.0005054, 0.0166448),
    449.0: (0.0031718, 0.0005377, 0.0166136),
    450.0: (0.0031448, 0.0005713, 0.0165785),
    451.0: (0.0031167, 0.0006062, 0.0165424),
    452.0: (0.0030871, 0.0006426, 0.0165030),
    453.0: (0.0030553, 0.0006803, 0.0164553),
    454.0: (0.0030202, 0.0007194, 0.0163947),
    455.0: (0.0029810, 0.0007598, 0.0163164),
    456.0: (0.0029373, 0.0008017, 0.0162178),
    457.0: (0.0028892, 0.0008449, 0.0160990),
    458.0: (0.0028368, 0.0008891, 0.0159594),
    459.0: (0.0027804, 0.0009342, 0.0157985),
    460.0: (0.0027200, 0.0009800, 0.0156157),
    461.0: (0.0026561, 0.0010264, 0.0154130),
    462.0: (0.0025883, 0.0010734, 0.0151874),
    463.0: (0.0025153, 0.0011211, 0.0149311),
    464.0: (0.0024358, 0.0011696, 0.0146365),
    465.0: (0.0023486, 0.0012190, 0.0142957),
    466.0: (0.0022527, 0.0012693, 0.0139029),
    467.0: (0.0021498, 0.0013205, 0.0134670),
    468.0: (0.0020427, 0.0013729, 0.0130026),
    469.0: (0.0019343, 0.0014269, 0.0125242),
    470.0: (0.0018271, 0.0014826, 0.0120461),
    471.0: (0.0017229, 0.0015401, 0.0115764),
    472.0: (0.0016210, 0.0015995, 0.0111124),
    473.0: (0.0015215, 0.0016608, 0.0106534),
    474.0: (0.0014242, 0.0017240, 0.0101986),
    475.0: (0.0013289, 0.0017891, 0.0097472),
    476.0: (0.0012361, 0.0018563, 0.0093009),
    477.0: (0.0011462, 0.0019256, 0.0088626),
    478.0: (0.0010593, 0.0019967, 0.0084333),
    479.0: (0.0009753, 0.0020690, 0.0080139),
    480.0: (0.0008943, 0.0021424, 0.0076053),
    481.0: (0.0008163, 0.0022166, 0.0072084),
    482.0: (0.0007416, 0.0022922, 0.0068241),
    483.0: (0.0006706, 0.0023700, 0.0064543),
    484.0: (0.0006038, 0.0024507, 0.0061006),
    485.0: (0.0005418, 0.0025351, 0.0057647),
    486.0: (0.0004848, 0.0026236, 0.0054478),
    487.0: (0.0004326, 0.0027165, 0.0051493),
    488.0: (0.0003847, 0.0028142, 0.0048679),
    489.0: (0.0003403, 0.0029173, 0.0046025),
    490.0: (0.0002992, 0.0030263, 0.0043519),
    491.0: (0.0002609, 0.0031418, 0.0041156),
    492.0: (0.0002256, 0.0032640, 0.0038935),
    493.0: (0.0001933, 0.0033928, 0.0036849),
    494.0: (0.0001638, 0.0035280, 0.0034890),
    495.0: (0.0001373, 0.0036695, 0.0033052),
    496.0: (0.0001135, 0.0038168, 0.0031327),
    497.0: (9.26e-05, 0.0039706, 0.0029708),
    498.0: (7.43e-05, 0.0041327, 0.0028191),
    499.0: (5.87e-05, 0.0043045, 0.0026772),
    500.0: (4.56e-05, 0.0044878, 0.0025446),
    501.0: (3.51e-05, 0.0046836, 0.0024213),
    502.0: (2.73e-05, 0.0048904, 0.0023059),
    503.0: (2.25e-05, 0.0051060, 0.0021963),
    504.0: (2.07e-05, 0.0053279, 0.0020905),
    505.0: (2.23e-05, 0.0055539, 0.0019861),
    506.0: (2.72e-05, 0.0057824, 0.0018820),
    507.0: (3.57e-05, 0.0060137, 0.0017786),
    508.0: (4.83e-05, 0.0062484, 0.0016767),
    509.0: (6.52e-05, 0.0064873, 0.0015769),
    510.0: (8.69e-05, 0.0067307, 0.0014800),
    511.0: (0.0001136, 0.0069786, 0.0013859),
    512.0: (0.0001453, 0.0072292, 0.0012945),
    513.0: (0.0001822, 0.0074806, 0.0012068),
    514.0: (0.0002244, 0.0077310, 0.0011233),
    515.0: (0.0002722, 0.0079785, 0.0010450),
    516.0: (0.0003257, 0.0082225, 0.0009721),
    517.0: (0.0003847, 0.0084618, 0.0009043),
    518.0: (0.0004490, 0.0086938, 0.0008418),
    519.0: (0.0005182, 0.0089159, 0.0007844),
    520.0: (0.0005920, 0.0091254, 0.0007320),
    521.0: (0.0006703, 0.0093204, 0.0006849),
    522.0: (0.0007529, 0.0095018, 0.0006425),
    523.0: (0.0008398, 0.0096712, 0.0006040),
    524.0: (0.0009307, 0.0098304, 0.0005687),
    525.0: (0.0010256, 0.0099812, 0.0005356),
    526.0: (0.0011245, 0.0101242, 0.0005043),
    527.0: (0.0012270, 0.0102587, 0.0004747),
    528.0: (0.0013323, 0.0103843, 0.0004467),
    529.0: (0.0014398, 0.0105006, 0.0004200),
    530.0: (0.0015488, 0.0106074, 0.0003944),
    531.0: (0.0016588, 0.0107046, 0.0003696),
    532.0: (0.0017700, 0.0107925, 0.0003455),
    533.0: (0.0018826, 0.0108717, 0.0003224),
    534.0: (0.0019967, 0.0109425, 0.0003002),
    535.0: (0.0021126, 0.0110054, 0.0002792),
    536.0: (0.0022303, 0.0110606, 0.0002592),
    537.0: (0.0023496, 0.0111082, 0.0002404),
    538.0: (0.0024705, 0.0111480, 0.0002225),
    539.0: (0.0025932, 0.0111802, 0.0002057),
    540.0: (0.0027177, 0.0112046, 0.0001899),
    541.0: (0.0028439, 0.0112213, 0.0001751),
    542.0: (0.0029720, 0.0112306, 0.0001613),
    543.0: (0.0031017, 0.0112326, 0.0001484),
    544.0: (0.0032332, 0.0112273, 0.0001364),
    545.0: (0.0033662, 0.0112149, 0.0001254),
    546.0: (0.0035008, 0.0111954, 0.0001151),
    547.0: (0.0036370, 0.0111690, 0.0001057),
    548.0: (0.0037750, 0.0111362, 9.71e-05),
    549.0: (0.0039147, 0.0110973, 8.91e-05),
    550.0: (0.0040564, 0.0110527, 8.19e-05),
    551.0: (0.0042000, 0.0110022, 7.52e-05),
    552.0: (0.0043454, 0.0109459, 6.91e-05),
    553.0: (0.0044926, 0.0108839, 6.35e-05),
    554.0: (0.0046415, 0.0108161, 5.84e-05),
    555.0: (0.0047920, 0.0107425, 5.38e-05),
    556.0: (0.0049440, 0.0106629, 4.96e-05),
    557.0: (0.0050975, 0.0105773, 4.58e-05),
    558.0: (0.0052520, 0.0104855, 4.24e-05),
    559.0: (0.0054075, 0.0103873, 3.93e-05),
    560.0: (0.0055636, 0.0102827, 3.65e-05),
    561.0: (0.0057201, 0.0101713, 3.39e-05),
    562.0: (0.0058769, 0.0100537, 3.15e-05),
    563.0: (0.0060339, 0.0099302, 2.94e-05),
    564.0: (0.0061913, 0.0098011, 2.75e-05),
    565.0: (0.0063488, 0.0096665, 2.57e-05),
    566.0: (0.0065063, 0.0095268, 2.42e-05),
    567.0: (0.0066637, 0.0093819, 2.28e-05),
    568.0: (0.0068207, 0.0092320, 2.16e-05),
    569.0: (0.0069769, 0.0090771, 2.06e-05),
    570.0: (0.0071321, 0.0089174, 1.96e-05),
    571.0: (0.0072859, 0.0087528, 1.89e-05),
    572.0: (0.0074383, 0.0085837, 1.82e-05),
    573.0: (0.0075890, 0.0084104, 1.77e-05),
    574.0: (0.0077378, 0.0082333, 1.72e-05),
    575.0: (0.0078845, 0.0080525, 1.68e-05),
    576.0: (0.0080289, 0.0078685, 1.65e-05),
    577.0: (0.0081707, 0.0076814, 1.63e-05),
    578.0: (0.0083093, 0.0074915, 1.60e-05),
    579.0: (0.0084443, 0.0072987, 1.57e-05),
    580.0: (0.0085751, 0.0071033, 1.54e-05),
    581.0: (0.0087015, 0.0069055, 1.51e-05),
    582.0: (0.0088231, 0.0067057, 1.46e-05),
    583.0: (0.0089399, 0.0065044, 1.42e-05),
    584.0: (0.0090516, 0.0063021, 1.36e-05),
    585.0: (0.0091582, 0.0060993, 1.31e-05),
    586.0: (0.0092591, 0.0058964, 1.25e-05),
    587.0: (0.0093542, 0.0056937, 1.19e-05),
    588.0: (0.0094435, 0.0054917, 1.13e-05),
    589.0: (0.0095269, 0.0052906, 1.07e-05),
    590.0: (0.0096046, 0.0050910, 1.03e-05),
    591.0: (0.0096765, 0.0048931, 1.00e-05),
    592.0: (0.0097420, 0.0046974, 9.80e-06),
    593.0: (0.0098000, 0.0045043, 9.70e-06),
    594.0: (0.0098494, 0.0043144, 9.60e-06),
    595.0: (0.0098891, 0.0041283, 9.40e-06),
    596.0: (0.0099180, 0.0039465, 9.10e-06),
    597.0: (0.0099368, 0.0037690, 8.70e-06),
    598.0: (0.0099462, 0.0035956, 8.30e-06),
    599.0: (0.0099472, 0.0034261, 7.90e-06),
    600.0: (0.0099405, 0.0032602, 7.50e-06),
    601.0: (0.0099268, 0.0030979, 7.10e-06),
    602.0: (0.0099054, 0.0029397, 6.80e-06),
    603.0: (0.0098752, 0.0027858, 6.40e-06),
    604.0: (0.0098355, 0.0026369, 6.00e-06),
    605.0: (0.0097852, 0.0024933, 5.60e-06),
    606.0: (0.0097238, 0.0023553, 5.10e-06),
    607.0: (0.0096519, 0.0022229, 4.60e-06),
    608.0: (0.0095705, 0.0020958, 4.10e-06),
    609.0: (0.0094805, 0.0019739, 3.60e-06),
    610.0: (0.0093828, 0.0018572, 3.20e-06),
    611.0: (0.0092776, 0.0017455, 2.90e-06),
    612.0: (0.0091650, 0.0016389, 2.60e-06),
    613.0: (0.0090448, 0.0015372, 2.50e-06),
    614.0: (0.0089172, 0.0014404, 2.40e-06),
    615.0: (0.0087819, 0.0013484, 2.20e-06),
    616.0: (0.0086396, 0.0012610, 2.10e-06),
    617.0: (0.0084904, 0.0011783, 2.10e-06),
    618.0: (0.0083337, 0.0010998, 2.00e-06),
    619.0: (0.0081692, 0.0010253, 1.90e-06),
    620.0: (0.0079963, 0.0009547, 1.80e-06),
    621.0: (0.0078151, 0.0008876, 1.60e-06),
    622.0: (0.0076266, 0.0008241, 1.50e-06),
    623.0: (0.0074323, 0.0007641, 1.30e-06),
    624.0: (0.0072336, 0.0007075, 1.10e-06),
    625.0: (0.0070319, 0.0006544, 9.00e-07),
    626.0: (0.0068278, 0.0006045, 8.00e-07),
    627.0: (0.0066219, 0.0005578, 7.00e-07),
    628.0: (0.0064162, 0.0005141, 6.00e-07),
    629.0: (0.0062122, 0.0004733, 5.00e-07),
    630.0: (0.0060119, 0.0004351, 5.00e-07),
    631.0: (0.0058164, 0.0003996, 4.00e-07),
    632.0: (0.0056255, 0.0003666, 4.00e-07),
    633.0: (0.0054382, 0.0003359, 3.00e-07),
    634.0: (0.0052538, 0.0003074, 3.00e-07),
    635.0: (0.0050713, 0.0002809, 3.00e-07),
    636.0: (0.0048907, 0.0002562, 3.00e-07),
    637.0: (0.0047124, 0.0002334, 2.00e-07),
    638.0: (0.0045364, 0.0002123, 2.00e-07),
    639.0: (0.0043628, 0.0001928, 2.00e-07),
    640.0: (0.0041916, 0.0001747, 2.00e-07),
    641.0: (0.0040228, 0.0001581, 2.00e-07),
    642.0: (0.0038566, 0.0001428, 2.00e-07),
    643.0: (0.0036932, 0.0001287, 1.00e-07),
    644.0: (0.0035331, 0.0001159, 1.00e-07),
    645.0: (0.0033765, 0.0001043, 1.00e-07),
    646.0: (0.0032236, 9.38e-05, 1.00e-07),
    647.0: (0.0030744, 8.43e-05, 1.00e-07),
    648.0: (0.0029294, 7.57e-05, 0.0000000),
    649.0: (0.0027888, 6.80e-05, 0.0000000),
    650.0: (0.0026531, 6.10e-05, 0.0000000),
    651.0: (0.0025225, 5.46e-05, 0.0000000),
    652.0: (0.0023969, 4.88e-05, 0.0000000),
    653.0: (0.0022759, 4.36e-05, 0.0000000),
    654.0: (0.0021592, 3.89e-05, 0.0000000),
    655.0: (0.0020467, 3.46e-05, 0.0000000),
    656.0: (0.0019381, 3.08e-05, 0.0000000),
    657.0: (0.0018335, 2.74e-05, 0.0000000),
    658.0: (0.0017329, 2.43e-05, 0.0000000),
    659.0: (0.0016362, 2.16e-05, 0.0000000),
    660.0: (0.0015432, 1.92e-05, 0.0000000),
    661.0: (0.0014540, 1.70e-05, 0.0000000),
    662.0: (0.0013685, 1.52e-05, 0.0000000),
    663.0: (0.0012867, 1.35e-05, 0.0000000),
    664.0: (0.0012086, 1.21e-05, 0.0000000),
    665.0: (0.0011342, 1.07e-05, 0.0000000),
    666.0: (0.0010635, 9.50e-06, 0.0000000),
    667.0: (0.0009963, 8.40e-06, 0.0000000),
    668.0: (0.0009329, 7.50e-06, 0.0000000),
    669.0: (0.0008734, 6.60e-06, 0.0000000),
    670.0: (0.0008179, 5.80e-06, 0.0000000),
    671.0: (0.0007665, 5.10e-06, 0.0000000),
    672.0: (0.0007188, 4.50e-06, 0.0000000),
    673.0: (0.0006745, 4.00e-06, 0.0000000),
    674.0: (0.0006334, 3.50e-06, 0.0000000),
    675.0: (0.0005952, 3.10e-06, 0.0000000),
    676.0: (0.0005597, 2.70e-06, 0.0000000),
    677.0: (0.0005267, 2.30e-06, 0.0000000),
    678.0: (0.0004957, 2.00e-06, 0.0000000),
    679.0: (0.0004662, 1.70e-06, 0.0000000),
    680.0: (0.0004377, 1.50e-06, 0.0000000),
    681.0: (0.0004097, 1.20e-06, 0.0000000),
    682.0: (0.0003825, 1.00e-06, 0.0000000),
    683.0: (0.0003563, 8.00e-07, 0.0000000),
    684.0: (0.0003313, 7.00e-07, 0.0000000),
    685.0: (0.0003079, 5.00e-07, 0.0000000),
    686.0: (0.0002860, 4.00e-07, 0.0000000),
    687.0: (0.0002656, 3.00e-07, 0.0000000),
    688.0: (0.0002465, 3.00e-07, 0.0000000),
    689.0: (0.0002288, 2.00e-07, 0.0000000),
    690.0: (0.0002124, 2.00e-07, 0.0000000),
    691.0: (0.0001973, 1.00e-07, 0.0000000),
    692.0: (0.0001834, 1.00e-07, 0.0000000),
    693.0: (0.0001707, 1.00e-07, 0.0000000),
    694.0: (0.0001590, 1.00e-07, 0.0000000),
    695.0: (0.0001482, 0.0000000, 0.0000000),
    696.0: (0.0001384, 0.0000000, 0.0000000),
    697.0: (0.0001294, 0.0000000, 0.0000000),
    698.0: (0.0001212, 0.0000000, 0.0000000),
    699.0: (0.0001135, 0.0000000, 0.0000000),
    700.0: (0.0001063, 0.0000000, 0.0000000),
    701.0: (9.95e-05, 0.0000000, 0.0000000),
    702.0: (9.30e-05, 0.0000000, 0.0000000),
    703.0: (8.69e-05, 0.0000000, 0.0000000),
    704.0: (8.12e-05, 0.0000000, 0.0000000),
    705.0: (7.59e-05, 0.0000000, 0.0000000),
    706.0: (7.10e-05, 0.0000000, 0.0000000),
    707.0: (6.63e-05, 0.0000000, 0.0000000),
    708.0: (6.20e-05, 0.0000000, 0.0000000),
    709.0: (5.80e-05, 0.0000000, 0.0000000),
    710.0: (5.42e-05, 0.0000000, 0.0000000),
    711.0: (5.06e-05, 0.0000000, 0.0000000),
    712.0: (4.73e-05, 0.0000000, 0.0000000),
    713.0: (4.41e-05, 0.0000000, 0.0000000),
    714.0: (4.12e-05, 0.0000000, 0.0000000),
    715.0: (3.85e-05, 0.0000000, 0.0000000),
    716.0: (3.59e-05, 0.0000000, 0.0000000),
    717.0: (3.35e-05, 0.0000000, 0.0000000),
    718.0: (3.12e-05, 0.0000000, 0.0000000),
    719.0: (2.91e-05, 0.0000000, 0.0000000),
    720.0: (2.71e-05, 0.0000000, 0.0000000),
    721.0: (2.53e-05, 0.0000000, 0.0000000),
    722.0: (2.36e-05, 0.0000000, 0.0000000),
    723.0: (2.20e-05, 0.0000000, 0.0000000),
    724.0: (2.06e-05, 0.0000000, 0.0000000),
    725.0: (1.92e-05, 0.0000000, 0.0000000),
    726.0: (1.79e-05, 0.0000000, 0.0000000),
    727.0: (1.67e-05, 0.0000000, 0.0000000),
    728.0: (1.55e-05, 0.0000000, 0.0000000),
    729.0: (1.45e-05, 0.0000000, 0.0000000),
    730.0: (1.35e-05, 0.0000000, 0.0000000),
    731.0: (1.25e-05, 0.0000000, 0.0000000),
    732.0: (1.17e-05, 0.0000000, 0.0000000),
    733.0: (1.08e-05, 0.0000000, 0.0000000),
    734.0: (1.01e-05, 0.0000000, 0.0000000),
    735.0: (9.40e-06, 0.0000000, 0.0000000),
    736.0: (8.70e-06, 0.0000000, 0.0000000),
    737.0: (8.10e-06, 0.0000000, 0.0000000),
    738.0: (7.50e-06, 0.0000000, 0.0000000),
    739.0: (7.00e-06, 0.0000000, 0.0000000),
    740.0: (6.50e-06, 0.0000000, 0.0000000),
    741.0: (6.00e-06, 0.0000000, 0.0000000),
    742.0: (5.60e-06, 0.0000000, 0.0000000),
    743.0: (5.20e-06, 0.0000000, 0.0000000),
    744.0: (4.80e-06, 0.0000000, 0.0000000),
    745.0: (4.50e-06, 0.0000000, 0.0000000),
    746.0: (4.10e-06, 0.0000000, 0.0000000),
    747.0: (3.90e-06, 0.0000000, 0.0000000),
    748.0: (3.60e-06, 0.0000000, 0.0000000),
    749.0: (3.30e-06, 0.0000000, 0.0000000),
    750.0: (3.10e-06, 0.0000000, 0.0000000),
    751.0: (2.90e-06, 0.0000000, 0.0000000),
    752.0: (2.70e-06, 0.0000000, 0.0000000),
    753.0: (2.50e-06, 0.0000000, 0.0000000),
    754.0: (2.40e-06, 0.0000000, 0.0000000),
    755.0: (2.20e-06, 0.0000000, 0.0000000),
    756.0: (2.10e-06, 0.0000000, 0.0000000),
    757.0: (1.90e-06, 0.0000000, 0.0000000),
    758.0: (1.80e-06, 0.0000000, 0.0000000),
    759.0: (1.70e-06, 0.0000000, 0.0000000),
    760.0: (1.60e-06, 0.0000000, 0.0000000),
    761.0: (1.50e-06, 0.0000000, 0.0000000),
    762.0: (1.40e-06, 0.0000000, 0.0000000),
    763.0: (1.30e-06, 0.0000000, 0.0000000),
    764.0: (1.20e-06, 0.0000000, 0.0000000),
    765.0: (1.10e-06, 0.0000000, 0.0000000),
    766.0: (1.00e-06, 0.0000000, 0.0000000),
    767.0: (1.00e-06, 0.0000000, 0.0000000),
    768.0: (9.00e-07, 0.0000000, 0.0000000),
    769.0: (8.00e-07, 0.0000000, 0.0000000),
    770.0: (8.00e-07, 0.0000000, 0.0000000),
    771.0: (7.00e-07, 0.0000000, 0.0000000),
    772.0: (7.00e-07, 0.0000000, 0.0000000),
    773.0: (6.00e-07, 0.0000000, 0.0000000),
    774.0: (6.00e-07, 0.0000000, 0.0000000),
    775.0: (5.00e-07, 0.0000000, 0.0000000),
    776.0: (5.00e-07, 0.0000000, 0.0000000),
    777.0: (5.00e-07, 0.0000000, 0.0000000),
    778.0: (4.00e-07, 0.0000000, 0.0000000),
    779.0: (4.00e-07, 0.0000000, 0.0000000),
    780.0: (4.00e-07, 0.0000000, 0.0000000),
    781.0: (4.00e-07, 0.0000000, 0.0000000),
    782.0: (3.00e-07, 0.0000000, 0.0000000),
    783.0: (3.00e-07, 0.0000000, 0.0000000),
    784.0: (3.00e-07, 0.0000000, 0.0000000),
    785.0: (3.00e-07, 0.0000000, 0.0000000),
    786.0: (3.00e-07, 0.0000000, 0.0000000),
    787.0: (2.00e-07, 0.0000000, 0.0000000),
    788.0: (2.00e-07, 0.0000000, 0.0000000),
    789.0: (2.00e-07, 0.0000000, 0.0000000),
    790.0: (2.00e-07, 0.0000000, 0.0000000),
    791.0: (2.00e-07, 0.0000000, 0.0000000),
    792.0: (2.00e-07, 0.0000000, 0.0000000),
    793.0: (2.00e-07, 0.0000000, 0.0000000),
    794.0: (1.00e-07, 0.0000000, 0.0000000),
    795.0: (1.00e-07, 0.0000000, 0.0000000),
    796.0: (1.00e-07, 0.0000000, 0.0000000),
    797.0: (1.00e-07, 0.0000000, 0.0000000),
    798.0: (1.00e-07, 0.0000000, 0.0000000),
    799.0: (1.00e-07, 0.0000000, 0.0000000),
    800.0: (1.00e-07, 0.0000000, 0.0000000),
    801.0: (1.00e-07, 0.0000000, 0.0000000),
    802.0: (1.00e-07, 0.0000000, 0.0000000),
    803.0: (1.00e-07, 0.0000000, 0.0000000),
    804.0: (1.00e-07, 0.0000000, 0.0000000),
    805.0: (1.00e-07, 0.0000000, 0.0000000),
    806.0: (1.00e-07, 0.0000000, 0.0000000),
    807.0: (1.00e-07, 0.0000000, 0.0000000),
    808.0: (1.00e-07, 0.0000000, 0.0000000),
    809.0: (1.00e-07, 0.0000000, 0.0000000),
    810.0: (0.0000000, 0.0000000, 0.0000000),
    811.0: (0.0000000, 0.0000000, 0.0000000),
    812.0: (0.0000000, 0.0000000, 0.0000000),
    813.0: (0.0000000, 0.0000000, 0.0000000),
    814.0: (0.0000000, 0.0000000, 0.0000000),
    815.0: (0.0000000, 0.0000000, 0.0000000),
    816.0: (0.0000000, 0.0000000, 0.0000000),
    817.0: (0.0000000, 0.0000000, 0.0000000),
    818.0: (0.0000000, 0.0000000, 0.0000000),
    819.0: (0.0000000, 0.0000000, 0.0000000),
    820.0: (0.0000000, 0.0000000, 0.0000000),
    821.0: (0.0000000, 0.0000000, 0.0000000),
    822.0: (0.0000000, 0.0000000, 0.0000000),
    823.0: (0.0000000, 0.0000000, 0.0000000),
    824.0: (0.0000000, 0.0000000, 0.0000000),
    825.0: (0.0000000, 0.0000000, 0.0000000),
    826.0: (0.0000000, 0.0000000, 0.0000000),
    827.0: (0.0000000, 0.0000000, 0.0000000),
    828.0: (0.0000000, 0.0000000, 0.0000000),
    829.0: (0.0000000, 0.0000000, 0.0000000),
    830.0: (0.0000000, 0.0000000, 0.0000000)
}

ACES_RICD = RGB_SpectralSensitivities(ACES_RICD_DATA, name='ACES RICD')
"""
*ACES Reference Input Capture Device* spectral sensitivities.

References
----------
:cite:`TheAcademyofMotionPictureArtsandSciences2014q`,
:cite:`TheAcademyofMotionPictureArtsandSciences2014r`,
:cite:`TheAcademyofMotionPictureArtsandSciencese`

ACES_RICD : RGB_SpectralSensitivities
"""
