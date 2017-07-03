import networkx as nx


def example30():
    G = nx.DiGraph()

    G.add_node(1, info='Bacteria')
    G.add_node(2, info='Epithelial cells', isEssential='0')
    G.add_node(3, info='Complement', isEssential='1')
    G.add_node(4, info='Ag-Ab complex', isEssential='1')
    G.add_node(5, info='Pro-inflamatory cytokines (IL-1,6,TNF-alpha, beta)', isEssential='0')
    G.add_node(6, info='Recruited PMNs', isEssential='1')
    G.add_node(7, info='Activated Phagocytic Cells', isEssential='0')
    G.add_node(8, info='Other antibodies', isEssential='1')
    G.add_node(9, info='Complement fixing antibodies IgG, IgM', isEssential='1')
    G.add_node(10, info='Macrophages', isEssential='1')
    G.add_node(11, info='Th1 cells', isEssential='1')
    G.add_node(12, info='T0 cells', isEssential='0')
    G.add_node(13, info='Th2 cells', isEssential='0')
    G.add_node(14, info='B cells', isEssential='0')
    G.add_node(15, info='Th1 related cytokines (IFN- Gamma, TNF-beta, IL-2)', isEssential='1')
    G.add_node(16, info='Th2 related cytokines (IL-4, 10,13)', isEssential='0')
    G.add_node(17, info='Dendritic cells', isEssential='0')
    G.add_node(18, info='Phagocytosis')

    G.add_edge(1, 17, weight=0)
    G.add_edge(1, 4, weight=0)
    G.add_edge(1, 2, weight=0)
    G.add_edge(1, 3, weight=0)

    G.add_edge(2, 5, weight=0)

    G.add_edge(3, 7, weight=0)

    G.add_edge(4, 3, weight=0)
    G.add_edge(4, 7, weight=0)

    G.add_edge(5, 17, weight=0)
    G.add_edge(5, 6, weight=0)
    G.add_edge(5, 10, weight=0)

    G.add_edge(6, 7, weight=0)

    G.add_edge(7, 5, weight=0)

    G.add_edge(8, 4, weight=0)
    G.add_edge(8, 8, weight=0)

    G.add_edge(9, 9, weight=0)
    G.add_edge(9, 3, weight=0)

    G.add_edge(10, 7, weight=0)

    G.add_edge(11, 15, weight=0)

    G.add_edge(12, 11, weight=0)
    G.add_edge(12, 13, weight=0)

    G.add_edge(13, 14, weight=0)
    G.add_edge(13, 16, weight=0)

    G.add_edge(14, 8, weight=0)
    G.add_edge(14, 9, weight=0)

    G.add_edge(15, 10, weight=0)
    G.add_edge(15, 17, weight=0)
    G.add_edge(15, 11, weight=0)
    G.add_edge(15, 16, weight=1)

    G.add_edge(16, 15, weight=1)
    G.add_edge(16, 5, weight=1)
    G.add_edge(16, 17, weight=0)
    G.add_edge(16, 13, weight=0)

    G.add_edge(17, 15, weight=0)
    G.add_edge(17, 16, weight=0)

    G.add_edge(18, 1, weight=1)
    return G


def example32S3():
    G = nx.DiGraph()
    G.add_node(1, info='CD28')
    G.add_node(2, info='CD4', isEssential='0')
    G.add_node(3, info='TCRlig')
    G.add_node(4, info='CD45', isEssential='0')
    G.add_node(5, info='TCRb', isEssential='1')
    G.add_node(6, info='SHP1', isEssential='0')
    G.add_node(7, info='Csk', isEssential='0')
    G.add_node(8, info='PAG', isEssential='0')
    G.add_node(9, info='Lckp2', isEssential='0')
    G.add_node(10, info='CbIb')
    G.add_node(11, info='Lckp1', isEssential='0')
    G.add_node(12, info='Fyn', isEssential='1')
    G.add_node(13, info='PI3K', isEssential='1')
    G.add_node(14, info='cCbIp1')
    G.add_node(15, info='SHIP-1')
    G.add_node(16, info='PIP3', isEssential='1')
    G.add_node(17, info='PDK1', isEssential='1')
    G.add_node(18, info='PTEN')
    G.add_node(19, info='PKB')
    G.add_node(20, info='TCRp', isEssential='1')
    G.add_node(21, info='SHP2')
    G.add_node(22, info='ABI', isEssential='1')
    G.add_node(23, info='Rlk', isEssential='0')
    G.add_node(24, info='cCbIp2', isEssential='0')
    G.add_node(25, info='Gab2', isEssential='0')
    G.add_node(26, info='ZAP70', isEssential='1')
    G.add_node(27, info='Ca', isEssential='1')
    G.add_node(28, info='CaM', isEssential='1')
    G.add_node(29, info='CaMK4')
    G.add_node(30, info='CaMK2', isEssential='1')
    G.add_node(31, info='cabin1')
    G.add_node(32, info='AKAP79')
    G.add_node(33, info='Calpr1')
    G.add_node(34, info='LAT', isEssential='1')
    G.add_node(35, info='SLP76', isEssential='1')
    G.add_node(36, info='Itk', isEssential='0')
    G.add_node(37, info='IP3', isEssential='1')
    G.add_node(38, info='Calcln')
    G.add_node(39, info='Vav1', isEssential='1')
    G.add_node(40, info='sh3bp2', isEssential='0')
    G.add_node(41, info='PLCgb', isEssential='1')
    G.add_node(42, info='PLCga', isEssential='1')
    G.add_node(43, info='DAG', isEssential='1')
    G.add_node(44, info='RasGRP1', isEssential='0')
    G.add_node(45, info='Vav3', isEssential='0')
    G.add_node(46, info='Grb2', isEssential='0')
    G.add_node(47, info='Sos', isEssential='0')
    G.add_node(48, info='GAPs')
    G.add_node(49, info='PKCth', isEssential='1')
    G.add_node(50, info='Rac1p1', isEssential='0')
    G.add_node(51, info='Rac1p2', isEssential='0')
    G.add_node(52, info='HPK1', isEssential='0')
    G.add_node(53, info='Cdc42', isEssential='0')
    G.add_node(54, info='Ras', isEssential='0')
    G.add_node(55, info='Ikkg', isEssential='1')
    G.add_node(56, info='MLK3', isEssential='0')
    G.add_node(57, info='MEKK1', isEssential='0')
    G.add_node(58, info='Raf', isEssential='0')
    G.add_node(59, info='CARD11')
    G.add_node(60, info='CARD11a', isEssential='1')
    G.add_node(61, info='Ikkab', isEssential='1')
    G.add_node(62, info='Gadd45')
    G.add_node(63, info='MKK4')
    G.add_node(64, info='MEK', isEssential='0')
    G.add_node(65, info='Bcl10')
    G.add_node(66, info='Malt1')
    G.add_node(67, info='IkB')
    G.add_node(68, info='p38')
    G.add_node(69, info='JNK')
    G.add_node(70, info='ERK', isEssential='0')
    G.add_node(71, info='SRE')
    G.add_node(72, info='Jun')
    G.add_node(73, info='Fos')
    G.add_node(74, info='Rsk')
    G.add_node(75, info='AP1')
    G.add_node(76, info='CREB')
    G.add_node(77, info='CRE')

    G.add_node(78, info='BAD')
    G.add_node(79, info='GSK3')
    G.add_node(80, info='NFkB')
    G.add_node(81, info='NFAT')
    G.add_node(82, info='bcat')
    G.add_node(83, info='Cyc1')
    G.add_node(84, info='p21c')
    G.add_node(85, info='p27k')
    G.add_node(86, info='FKHR')
    G.add_node(87, info='BclXL')
    G.add_node(88, info='p70S6K')
    G.add_node(132, info='Gads', isEssential='1')
    G.add_node(133, info='DGK', isEssential='0')

    G.add_edge(1, 10, weight=1)
    G.add_edge(1, 39, weight=0)
    G.add_edge(1, 13, weight=0)

    G.add_edge(2, 11, weight=0)

    G.add_edge(3, 5, weight=0)

    G.add_edge(4, 11, weight=0)
    G.add_edge(4, 12, weight=0)

    G.add_edge(5, 20, weight=0)
    G.add_edge(5, 12, weight=0)
    G.add_edge(5, 9, weight=0)
    G.add_edge(5, 133, weight=0)
    G.add_edge(5, 8, weight=1)

    G.add_edge(6, 11, weight=1)

    G.add_edge(7, 11, weight=1)

    G.add_edge(8, 7, weight=0)

    G.add_edge(9, 12, weight=0)
    G.add_edge(9, 13, weight=0)

    G.add_edge(10, 13, weight=1)

    G.add_edge(11, 6, weight=0)
    G.add_edge(11, 12, weight=0)
    G.add_edge(11, 23, weight=0)
    G.add_edge(11, 22, weight=0)

    G.add_edge(12, 8, weight=0)
    G.add_edge(12, 24, weight=0)
    G.add_edge(12, 20, weight=0)
    G.add_edge(12, 22, weight=0)

    G.add_edge(13, 16, weight=0)

    G.add_edge(14, 5, weight=1)
    G.add_edge(14, 26, weight=1)

    G.add_edge(15, 16, weight=1)

    G.add_edge(16, 17, weight=0)
    G.add_edge(16, 36, weight=0)

    G.add_edge(17, 19, weight=0)
    G.add_edge(17, 88, weight=0)
    G.add_edge(17, 49, weight=0)

    G.add_edge(18, 16, weight=1)

    G.add_edge(19, 79, weight=1)
    G.add_edge(19, 78, weight=1)
    G.add_edge(19, 84, weight=1)
    G.add_edge(19, 85, weight=1)
    G.add_edge(19, 86, weight=1)

    G.add_edge(20, 26, weight=0)

    # no outgoing edges for node 21

    G.add_edge(22, 70, weight=0)

    G.add_edge(23, 42, weight=0)

    G.add_edge(24, 42, weight=1)

    G.add_edge(25, 21, weight=0)
    G.add_edge(25, 35, weight=1)

    G.add_edge(26, 14, weight=0)
    G.add_edge(26, 25, weight=0)
    G.add_edge(26, 39, weight=0)
    G.add_edge(26, 40, weight=0)

    G.add_edge(27, 28, weight=0)

    G.add_edge(28, 29, weight=0)
    G.add_edge(28, 30, weight=0)
    G.add_edge(28, 38, weight=0)

    G.add_edge(29, 31, weight=1)

    G.add_edge(30, 61, weight=0)

    G.add_edge(31, 38, weight=1)

    G.add_edge(32, 38, weight=1)

    G.add_edge(33, 38, weight=1)

    G.add_edge(34, 25, weight=0)
    G.add_edge(34, 40, weight=0)
    G.add_edge(34, 41, weight=0)
    G.add_edge(34, 46, weight=0)
    G.add_edge(34, 52, weight=0)

    G.add_edge(35, 42, weight=0)

    G.add_edge(36, 42, weight=0)

    G.add_edge(37, 27, weight=0)

    G.add_edge(38, 81, weight=0)

    G.add_edge(39, 50, weight=0)
    G.add_edge(39, 49, weight=0)

    G.add_edge(40, 45, weight=0)

    G.add_edge(41, 42, weight=0)

    G.add_edge(42, 43, weight=0)
    G.add_edge(42, 37, weight=0)

    G.add_edge(43, 44, weight=0)
    G.add_edge(43, 49, weight=0)

    G.add_edge(44, 54, weight=0)

    G.add_edge(45, 51, weight=0)

    G.add_edge(46, 25, weight=0)
    G.add_edge(46, 47, weight=0)

    G.add_edge(47, 53, weight=0)
    G.add_edge(47, 54, weight=0)

    G.add_edge(48, 54, weight=1)

    G.add_edge(49, 55, weight=0)

    G.add_edge(50, 56, weight=0)

    G.add_edge(51, 71, weight=0)
    G.add_edge(51, 57, weight=0)

    G.add_edge(52, 56, weight=0)
    G.add_edge(52, 56, weight=0)

    G.add_edge(53, 57, weight=0)
    G.add_edge(53, 71, weight=0)

    G.add_edge(54, 58, weight=0)

    G.add_edge(55, 61, weight=0)

    G.add_edge(56, 63, weight=0)

    G.add_edge(57, 68, weight=0)
    G.add_edge(57, 69, weight=0)

    G.add_edge(58, 64, weight=0)

    G.add_edge(59, 60, weight=0)

    G.add_edge(60, 55, weight=0)

    G.add_edge(61, 67, weight=1)

    G.add_edge(62, 68, weight=1)

    G.add_edge(63, 69, weight=0)

    G.add_edge(64, 70, weight=0)

    G.add_edge(65, 60, weight=0)

    G.add_edge(66, 60, weight=0)

    G.add_edge(67, 80, weight=1)

    # 68 no outgoing edges

    G.add_edge(69, 72, weight=0)

    G.add_edge(70, 73, weight=0)
    G.add_edge(70, 74, weight=0)

    # 71 no outgoing edgse

    G.add_edge(72, 75, weight=0)

    G.add_edge(73, 75, weight=0)

    G.add_edge(74, 76, weight=0)

    # 75 no outgoing edges

    G.add_edge(76, 77, weight=0)

    # 77 no outgoing edges

    G.add_edge(78, 87, weight=1)

    G.add_edge(79, 82, weight=1)
    G.add_edge(79, 83, weight=1)

    # 80 - 88 no outgoing edges

    G.add_edge(132, 35, weight=0)
    G.add_edge(132, 25, weight=0)

    G.add_edge(133, 43, weight=1)

    return G


def example32S4():
    G = nx.DiGraph()
    G.add_node(1, info='CD28')
    G.add_node(2, info='CD4', isEssential='0')
    G.add_node(3, info='TCRlig')
    G.add_node(4, info='CD45', isEssential='0')
    G.add_node(5, info='TCRb', isEssential='1')
    G.add_node(6, info='SHP1', isEssential='0')
    G.add_node(7, info='Csk', isEssential='0')
    G.add_node(8, info='PAG', isEssential='0')
    G.add_node(9, info='Lckp2', isEssential='0')
    G.add_node(10, info='CbIb')
    G.add_node(11, info='Lckp1', isEssential='0')
    G.add_node(12, info='Fyn', isEssential='1')
    G.add_node(13, info='PI3K', isEssential='1')
    G.add_node(14, info='cCbIp1', isEssential='0')
    G.add_node(15, info='SHIP-1')
    G.add_node(16, info='PIP3', isEssential='1')
    G.add_node(17, info='PDK1')
    G.add_node(18, info='PTEN')
    G.add_node(19, info='PKB')
    G.add_node(20, info='TCRp', isEssential='1')
    G.add_node(21, info='SHP2')
    G.add_node(22, info='ABI', isEssential='1')
    G.add_node(23, info='Rlk', isEssential='0')
    G.add_node(24, info='cCbIp2', isEssential='0')
    G.add_node(25, info='Gab2', isEssential='0')
    G.add_node(26, info='ZAP70', isEssential='1')
    G.add_node(27, info='Ca')
    G.add_node(28, info='CaM')
    G.add_node(29, info='CaMK4')
    G.add_node(30, info='CaMK2')
    G.add_node(31, info='cabin1')
    G.add_node(32, info='AKAP79')
    G.add_node(33, info='Calpr1')
    G.add_node(34, info='LAT', isEssential='1')
    G.add_node(35, info='SLP76', isEssential='1')
    G.add_node(36, info='Itk', isEssential='0')
    G.add_node(37, info='IP3')
    G.add_node(38, info='Calcln')
    G.add_node(39, info='Vav1', isEssential='1')
    G.add_node(40, info='sh3bp2', isEssential='0')
    G.add_node(41, info='PLCgb', isEssential='1')
    G.add_node(42, info='PLCga', isEssential='1')
    G.add_node(43, info='DAG', isEssential='1')
    G.add_node(44, info='RasGRP1', isEssential='1')
    G.add_node(45, info='Vav3', isEssential='0')
    G.add_node(46, info='Grb2', isEssential='1')
    G.add_node(47, info='Sos', isEssential='1')
    G.add_node(48, info='GAPs')
    G.add_node(49, info='PKCth')
    G.add_node(50, info='Rac1p1', isEssential='0')
    G.add_node(51, info='Rac1p2', isEssential='0')
    G.add_node(52, info='HPK1', isEssential='0')
    G.add_node(53, info='Cdc42', isEssential='0')
    G.add_node(54, info='Ras', isEssential='1')
    G.add_node(55, info='Ikkg')
    G.add_node(56, info='MLK3', isEssential='0')
    G.add_node(57, info='MEKK1', isEssential='0')
    G.add_node(58, info='Raf', isEssential='1')
    G.add_node(59, info='CARD11')
    G.add_node(60, info='CARD11a')
    G.add_node(61, info='Ikkab')
    G.add_node(62, info='Gadd45')
    G.add_node(63, info='MKK4', isEssential='0')
    G.add_node(64, info='MEK', isEssential='1')
    G.add_node(65, info='Bcl10')
    G.add_node(66, info='Malt1')
    G.add_node(67, info='IkB')
    G.add_node(68, info='p38')
    G.add_node(69, info='JNK', isEssential='1')
    G.add_node(70, info='ERK', isEssential='1')
    G.add_node(71, info='SRE')
    G.add_node(72, info='Jun', isEssential='1')
    G.add_node(73, info='Fos', isEssential='1')
    G.add_node(74, info='Rsk')
    G.add_node(75, info='AP1')
    G.add_node(76, info='CREB')
    G.add_node(77, info='CRE')

    G.add_node(78, info='BAD')
    G.add_node(79, info='GSK3')
    G.add_node(80, info='NFkB')
    G.add_node(81, info='NFAT')
    G.add_node(82, info='bcat')
    G.add_node(83, info='Cyc1')
    G.add_node(84, info='p21c')
    G.add_node(85, info='p27k')
    G.add_node(86, info='FKHR')
    G.add_node(87, info='BclXL')
    G.add_node(88, info='p70S6K')

    G.add_node(132, info='Gads', isEssential='1')
    G.add_node(133, info='DGK', isEssential='0')

    G.add_edge(1, 10, weight=1)
    G.add_edge(1, 39, weight=0)
    G.add_edge(1, 13, weight=0)

    G.add_edge(2, 11, weight=0)

    G.add_edge(3, 5, weight=0)

    G.add_edge(4, 11, weight=0)
    G.add_edge(4, 12, weight=0)

    G.add_edge(5, 20, weight=0)
    G.add_edge(5, 12, weight=0)
    G.add_edge(5, 9, weight=0)
    G.add_edge(5, 133, weight=0)
    G.add_edge(5, 8, weight=1)

    G.add_edge(6, 11, weight=1)

    G.add_edge(7, 11, weight=1)

    G.add_edge(8, 7, weight=0)

    G.add_edge(9, 12, weight=0)
    G.add_edge(9, 13, weight=0)

    G.add_edge(10, 13, weight=1)

    G.add_edge(11, 6, weight=0)
    G.add_edge(11, 12, weight=0)
    G.add_edge(11, 23, weight=0)
    G.add_edge(11, 22, weight=0)

    G.add_edge(12, 8, weight=0)
    G.add_edge(12, 24, weight=0)
    G.add_edge(12, 20, weight=0)
    G.add_edge(12, 22, weight=0)

    G.add_edge(13, 16, weight=0)

    G.add_edge(14, 5, weight=1)
    G.add_edge(14, 26, weight=1)

    G.add_edge(15, 16, weight=1)

    G.add_edge(16, 17, weight=0)
    G.add_edge(16, 36, weight=0)

    G.add_edge(17, 19, weight=0)
    G.add_edge(17, 88, weight=0)
    G.add_edge(17, 49, weight=0)

    G.add_edge(18, 16, weight=1)

    G.add_edge(19, 79, weight=1)
    G.add_edge(19, 78, weight=1)
    G.add_edge(19, 84, weight=1)
    G.add_edge(19, 85, weight=1)
    G.add_edge(19, 86, weight=1)

    G.add_edge(20, 26, weight=0)

    # no outgoing edges for node 21

    G.add_edge(22, 70, weight=0)

    G.add_edge(23, 42, weight=0)

    G.add_edge(24, 42, weight=1)

    G.add_edge(25, 21, weight=0)
    G.add_edge(25, 35, weight=1)

    G.add_edge(26, 14, weight=0)
    G.add_edge(26, 25, weight=0)
    G.add_edge(26, 39, weight=0)
    G.add_edge(26, 40, weight=0)

    G.add_edge(27, 28, weight=0)

    G.add_edge(28, 29, weight=0)
    G.add_edge(28, 30, weight=0)
    G.add_edge(28, 38, weight=0)

    G.add_edge(29, 31, weight=1)

    G.add_edge(30, 61, weight=0)

    G.add_edge(31, 38, weight=1)

    G.add_edge(32, 38, weight=1)

    G.add_edge(33, 38, weight=1)

    G.add_edge(34, 25, weight=0)
    G.add_edge(34, 40, weight=0)
    G.add_edge(34, 41, weight=0)
    G.add_edge(34, 46, weight=0)
    G.add_edge(34, 52, weight=0)

    G.add_edge(35, 42, weight=0)

    G.add_edge(36, 42, weight=0)

    G.add_edge(37, 27, weight=0)

    G.add_edge(38, 81, weight=0)

    G.add_edge(39, 50, weight=0)
    G.add_edge(39, 49, weight=0)

    G.add_edge(40, 45, weight=0)

    G.add_edge(41, 42, weight=0)

    G.add_edge(42, 43, weight=0)
    G.add_edge(42, 37, weight=0)

    G.add_edge(43, 44, weight=0)
    G.add_edge(43, 49, weight=0)

    G.add_edge(44, 54, weight=0)

    G.add_edge(45, 51, weight=0)

    G.add_edge(46, 25, weight=0)
    G.add_edge(46, 47, weight=0)

    G.add_edge(47, 53, weight=0)
    G.add_edge(47, 54, weight=0)

    G.add_edge(48, 54, weight=1)

    G.add_edge(49, 55, weight=0)

    G.add_edge(50, 56, weight=0)

    G.add_edge(51, 71, weight=0)
    G.add_edge(51, 57, weight=0)

    G.add_edge(52, 56, weight=0)
    G.add_edge(52, 56, weight=0)

    G.add_edge(53, 57, weight=0)
    G.add_edge(53, 71, weight=0)

    G.add_edge(54, 58, weight=0)

    G.add_edge(55, 61, weight=0)

    G.add_edge(56, 63, weight=0)

    G.add_edge(57, 68, weight=0)
    G.add_edge(57, 69, weight=0)

    G.add_edge(58, 64, weight=0)

    G.add_edge(59, 60, weight=0)

    G.add_edge(60, 55, weight=0)

    G.add_edge(61, 67, weight=1)

    G.add_edge(62, 68, weight=1)

    G.add_edge(63, 69, weight=0)

    G.add_edge(64, 70, weight=0)

    G.add_edge(65, 60, weight=0)

    G.add_edge(66, 60, weight=0)

    G.add_edge(67, 80, weight=1)

    # 68 no outgoing edges

    G.add_edge(69, 72, weight=0)

    G.add_edge(70, 73, weight=0)
    G.add_edge(70, 74, weight=0)

    # 71 no outgoing edgse

    G.add_edge(72, 75, weight=0)

    G.add_edge(73, 75, weight=0)

    G.add_edge(74, 76, weight=0)

    # 75 no outgoing edges

    G.add_edge(76, 77, weight=0)

    # 77 no outgoing edges

    G.add_edge(78, 87, weight=1)

    G.add_edge(79, 82, weight=1)
    G.add_edge(79, 83, weight=1)

    # 80 - 88 no outgoing edges

    G.add_edge(132, 35, weight=0)
    G.add_edge(132, 25, weight=0)

    G.add_edge(133, 43, weight=1)

    return G


def example31S2():
    G = nx.DiGraph()
    G.add_node(1, info='ABA')
    G.add_node(2, info='PEPC')

    G.add_node(3, info='RCN1', isEssential='0')

    G.add_node(4, info='NOS', isEssential='0')
    G.add_node(5, info='Arg')
    G.add_node(6, info='NIA12', isEssential='0')
    G.add_node(7, info='Nitrite')
    G.add_node(8, info='NADPH')

    G.add_node(9, info='Sph')
    G.add_node(10, info='SphK', isEssential='1')
    G.add_node(11, info='Malate')
    G.add_node(12, info='NO', isEssential='0')
    G.add_node(13, info='S1P', isEssential='1')
    G.add_node(14, info='OST1', isEssential='1')
    G.add_node(15, info='GCR1')
    G.add_node(16, info='GPA1', isEssential='1')
    G.add_node(17, info='AGB1', isEssential='1')

    G.add_node(18, info='PLC', isEssential='0')
    G.add_node(19, info='PIP2')
    G.add_node(20, info='NAD+')
    G.add_node(21, info='ADPRc', isEssential='0')
    G.add_node(22, info='GTP')
    G.add_node(23, info='GC', isEssential='0')
    G.add_node(24, info='InsPK', isEssential='0')

    G.add_node(25, info='PLD', isEssential='1')
    G.add_node(26, info='PC')
    G.add_node(27, info='NADPH')
    G.add_node(28, info='Atrboh', isEssential='1')
    G.add_node(29, info='DAG')
    G.add_node(30, info='InsP3', isEssential='0')
    G.add_node(31, info='cADPR', isEssential='0')
    G.add_node(32, info='cGMP', isEssential='0')
    G.add_node(33, info='InsP6', isEssential='0')
    G.add_node(34, info='RAC1')
    G.add_node(35, info='PA', isEssential='1')
    G.add_node(36, info='ROS', isEssential='1')
    G.add_node(37, info='CIS', isEssential='0')
    G.add_node(38, info='ABH1', isEssential='0')
    G.add_node(39, info='ROP2', isEssential='1')
    G.add_node(40, info='Actin', isEssential='1')
    G.add_node(41, info='ABI1', isEssential='0')
    G.add_node(42, info='pHc', isEssential='1')
    G.add_node(43, info='ROP10')
    G.add_node(44, info='ERA1', isEssential='0')
    G.add_node(45, info='CaIM', isEssential='0')
    G.add_node(46, info='H+ATPase', isEssential='0')

    G.add_node(47, info='Ca2+ATPase', isEssential='0')
    G.add_node(48, info='Ca2+', isEssential='1')
    G.add_node(49, info='KEV', isEssential='0')
    G.add_node(50, info='Depolar', isEssential='1')
    G.add_node(51, info='AnionEM', isEssential='1')
    G.add_node(52, info='KAP', isEssential='0')
    G.add_node(53, info='KOUT', isEssential='1')
    G.add_node(54, info='AtPP2C')
    G.add_node(55, info='Closure')

    G.add_edge(1, 18, weight=0)
    G.add_edge(1, 3, weight=0)
    G.add_edge(1, 24, weight=0)
    G.add_edge(1, 34, weight=1)
    G.add_edge(1, 10, weight=0)
    G.add_edge(1, 14, weight=0)
    G.add_edge(1, 42, weight=0)
    G.add_edge(1, 11, weight=1)
    G.add_edge(1, 2, weight=1)

    G.add_edge(2, 11, weight=0)

    G.add_edge(3, 6, weight=0)

    G.add_edge(4, 12, weight=0)
    G.add_edge(5, 12, weight=0)
    G.add_edge(6, 12, weight=0)
    G.add_edge(7, 12, weight=0)
    G.add_edge(8, 12, weight=0)

    G.add_edge(9, 13, weight=0)
    G.add_edge(10, 13, weight=0)

    G.add_edge(11, 55, weight=1)

    G.add_edge(12, 21, weight=0)
    G.add_edge(13, 16, weight=0)

    G.add_edge(14, 28, weight=0)

    G.add_edge(15, 16, weight=1)

    G.add_edge(16, 25, weight=0)

    G.add_edge(17, 16, weight=0)

    G.add_edge(18, 29, weight=0)
    G.add_edge(18, 30, weight=0)

    G.add_edge(19, 29, weight=0)
    G.add_edge(19, 30, weight=0)

    G.add_edge(20, 31, weight=0)

    G.add_edge(21, 31, weight=0)

    G.add_edge(22, 32, weight=0)

    G.add_edge(23, 32, weight=0)

    G.add_edge(24, 33, weight=0)

    G.add_edge(25, 35, weight=0)

    G.add_edge(26, 35, weight=0)

    G.add_edge(27, 36, weight=0)

    G.add_edge(28, 36, weight=0)

    # node 29 has no out edges

    G.add_edge(30, 37, weight=0)

    G.add_edge(31, 37, weight=0)

    G.add_edge(32, 37, weight=0)

    G.add_edge(33, 37, weight=0)

    G.add_edge(34, 40, weight=1)

    G.add_edge(35, 39, weight=0)
    G.add_edge(35, 41, weight=1)

    G.add_edge(36, 45, weight=0)
    G.add_edge(36, 46, weight=1)
    G.add_edge(36, 41, weight=1)
    G.add_edge(36, 53, weight=1)

    G.add_edge(37, 48, weight=0)

    G.add_edge(38, 45, weight=1)

    G.add_edge(39, 28, weight=0)

    G.add_edge(40, 55, weight=0)

    G.add_edge(41, 34, weight=0)
    G.add_edge(41, 28, weight=1)
    G.add_edge(41, 51, weight=1)

    G.add_edge(42, 28, weight=0)
    G.add_edge(42, 41, weight=0)
    G.add_edge(42, 46, weight=1)
    G.add_edge(42, 53, weight=0)
    G.add_edge(42, 52, weight=1)
    G.add_edge(42, 51, weight=0)

    # node 43 has not out edges

    G.add_edge(44, 43, weight=0)
    G.add_edge(44, 45, weight=1)

    G.add_edge(45, 48, weight=0)

    G.add_edge(46, 50, weight=1)

    G.add_edge(47, 48, weight=1)

    G.add_edge(48, 47, weight=0)
    G.add_edge(48, 18, weight=0)
    G.add_edge(48, 4, weight=0)
    G.add_edge(48, 52, weight=1)
    G.add_edge(48, 50, weight=0)
    G.add_edge(48, 49, weight=0)
    G.add_edge(48, 51, weight=0)
    G.add_edge(48, 46, weight=1)
    G.add_edge(48, 40, weight=0)

    G.add_edge(49, 50, weight=0)

    G.add_edge(50, 45, weight=1)
    G.add_edge(50, 52, weight=0)
    G.add_edge(50, 53, weight=0)

    G.add_edge(51, 50, weight=0)
    G.add_edge(51, 11, weight=1)
    G.add_edge(51, 55, weight=0)

    G.add_edge(52, 50, weight=1)
    G.add_edge(52, 55, weight=0)

    G.add_edge(53, 50, weight=1)
    G.add_edge(53, 55, weight=0)

    G.add_edge(54, 55, weight=1)

    # node 55 has no out edges

    return G


def generate_graph_test_loops():
    G = nx.DiGraph()
    G.add_edge(1, 2, weight=0)
    G.add_edge(2, 3, weight=0)
    G.add_edge(3, 4, weight=0)
    G.add_edge(3, 2, weight=1)
    return G


def composite_graph_1():
    G = nx.DiGraph()
    G.add_edge(1, 4, weight=0)
    G.add_edge(2, 4, weight=0)
    G.add_edge(3, 4, weight=0)
    G.add_edge(4, 5, weight=0)
    G.add_edge(4, 6, weight=0)
    G.add_edge(7, 6, weight=0)
    G.add_edge(6, 8, weight=0)
    return G


def composite_graph_1():
    G = nx.DiGraph()
    G.add_edge(1, 3, weight=0)
    G.add_edge(1, 4, weight=0)
    G.add_edge(2, 4, weight=0)
    return G


def generate_barabasi(n):
    import random
    G = nx.barabasi_albert_graph(n, 2, seed=14)
    # set info ( information about a node )
    for i in range(len(G.nodes())):
        G.node[i]['info'] = '_%s_' % i

    percent_chance_of_inhibited_edge = 25
    for u, v, d in G.edges(data=True):
        d['weight'] = random.choice(
            [0] * (100 - percent_chance_of_inhibited_edge) + [1] * percent_chance_of_inhibited_edge)

    diff = list(set(G.edges()) - set(G.to_directed()))
    G = G.to_directed()
    for u, v in diff:
        G.remove_edge(u, v)
    return G


def generate_graph():
    G = nx.DiGraph()
    G.add_edge(1, 2, weight=0)
    G.add_edge(3, 2, weight=1)
    G.add_edge(3, 6, weight=0)
    G.add_edge(2, 4, weight=1)
    G.add_edge(5, 4, weight=0)

    G.node[1]['info'] = 'A'
    G.node[3]['info'] = 'B'
    G.node[2]['info'] = 'C'
    G.node[4]['info'] = 'E'
    G.node[5]['info'] = 'D'
    G.node[6]['info'] = 'F'
    return G


def generate_graph_test_combine():
    G = nx.DiGraph()
    G.add_edge(1, 2, weight=0)
    G.add_edge(3, 2, weight=1)
    G.add_edge(2, 4, weight=1)
    G.add_edge(5, 4, weight=0)
    return G


def generate_graph_test_combine1():
    G = nx.DiGraph()
    G.add_edge(3, 2, weight=1)
