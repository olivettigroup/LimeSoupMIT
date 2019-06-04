from LimeSoup.ElsevierSoup import ElsevierSoup

from LimeSoup.test.soup_tester import SoupTester


class TestParsing(SoupTester):
    Soup = ElsevierSoup

    def test_paper_regular(self):
        parsed = self.get_parsed('10.1016-j.chroma.2013.12.003.xml', __file__)

        self.assertJournalEqual(parsed, 'Journal of Chromatography A')
        self.assertTitleEqual(
            parsed,
            'Accurate measurements of the true column efficiency and of the instrument '
            'band broadening contributions in the presence of a chromatographic column')
        self.assertKeywordsEqual(
            parsed, [
                'Column efficiency',
                'Intrinsic efficiency',
                'vHPLC systems',
                'Homologous compounds',
                'Extra-column band broadening',
                'Sub-2μm core–shell particles',
            ]
        )
        self.assertSectionPathsEqual(
            parsed, [
                ('$$Abstract', 1),
                ('$$Introduction', 4),
                ('$$Theory$$Band variance under isocratic and quasi-isocratic conditions', 2),
                ('$$Theory$$Relationship between the apparent and the intrinsic HETP', 4),
                ('$$Experimental$$Chemicals', 1),
                ('$$Experimental$$Instruments', 21),
                ('$$Experimental$$Columns', 1),
                ('$$Experimental$$Total porosities', 1),
                ('$$Experimental$$Peak first and second central moments', 3),
                ('$$Experimental$$HETP measurements', 2),
                ('$$Results and discussion', 1),
                ('$$Results and discussion'
                 '$$Difficulties in estimating the true column and instrument performance', 2),
                ('$$Results and discussion'
                 '$$Validation of a method estimating the true column and instrument performance', 12),
                ('$$Results and discussion'
                 '$$Application of the method to the determination of the intrinsic efficiency '
                 'of 2.1 mm × 100 mm column packed with prototype 1.6 μm core–shell particles', 2),
                ('$$Conclusion', 3),
            ]
        )

    def test_paper_abs_only(self):
        parsed = self.get_parsed('10.1006-jcis.1997.5095.xml', __file__)

        self.assertJournalEqual(parsed, 'Journal of Colloid and Interface Science')
        self.assertTitleEqual(
            parsed,
            '2-D and 3-D Interactions in Random Sequential Adsorption of Charged Particles')
        self.assertKeywordsEqual(
            parsed, [
                'colloidal electrostatic interactions',
                'superposition approximation',
                'simulation',
            ]
        )
        self.assertSectionPathsEqual(
            parsed, [
                ('$$Abstract', 1),
            ]
        )

    def test_paper_paper_with_list(self):
        parsed = self.get_parsed('10.1016-j.apsusc.2009.04.100.xml', __file__)

        self.assertJournalEqual(parsed, 'Applied Surface Science')
        self.assertTitleEqual(
            parsed,
            'Laser-assisted micro-forming process with miniaturised structures in sapphire dies')
        self.assertKeywordsEqual(
            parsed, [
                'Laser treatment',
                'Sapphire dies',
                'Miniaturisation',
                'Micro-forming',
                'Size effects',
            ]
        )
        self.assertSectionPathsEqual(
            parsed, [
                ('$$Abstract', 1),
                ('$$Introduction', 2),
                ('$$Die structures made using rotation masks', 4),
                ('$$Micro-forming', 8),
                ('$$Experimental set-up for laser-assisted micro-forming', 2),
                ('$$Conclusion', 1),
            ]
        )

    def test_paper_with_equations(self):
        parsed = self.get_parsed('10.1016-j.jiec.2013.10.024.xml', __file__)

        self.assertJournalEqual(parsed, 'Journal of Industrial and Engineering Chemistry')
        self.assertTitleEqual(
            parsed,
            'Adsorption of Cu(II) from aqueous solution by micro-structured ZnO thin films')
        self.assertKeywordsEqual(
            parsed, [
                'ZnO',
                'Micro-structure',
                'Thin film',
                'Adsorption',
                'Copper ion',
            ]
        )
        self.assertSectionPathsEqual(
            parsed, [
                ('$$Abstract', 1),
                ('$$Introduction', 4),
                ('$$Experimental methods', 8),
                ('$$Results$$Effect of pH on the film structure', 8),
                ('$$Results$$Effect of MW irradiation time on the film structure', 4),
                ('$$Results$$Surface area measurement', 2),
                ('$$Results$$Adsorption studies', 4),
                ('$$Results$$Point of zero charge pH', 1),
                ('$$Results$$The effect of pH on the removal efficiency', 2),
                ('$$Results$$Comparison with other adsorbents', 1),
                ('$$Conclusion', 3),
            ]
        )

    def test_paper_no_headings(self):
        parsed = self.get_parsed('10.1016-S0168-9002(01)01806-X.xml', __file__)

        self.assertJournalEqual(parsed, 'Nuclear Instruments and Methods in Physics Research Section A: '
                                        'Accelerators, Spectrometers, Detectors and Associated Equipment')
        self.assertTitleEqual(
            parsed,
            'List of participants')
        self.assertKeywordsEqual(
            parsed, []
        )
        self.assertSectionPathsEqual(
            parsed, [
                ('$$', 234),
            ]
        )

    def test_paper_no_full_text(self):
        parsed = self.get_parsed('10.1016-j.phpro.2013.10.018.xml', __file__)

        self.assertJournalEqual(parsed, 'Physics Procedia')
        self.assertTitleEqual(
            parsed,
            'Electrical and Optical Spectroscopic Study of Gd Doped GaN Epitaxial Layers')
        self.assertKeywordsEqual(
            parsed, [
                'Dilute magnetic semiconductors',
                'ferromagnetism',
                'point defects',
                'photoluminescence.']
        )
        self.assertSectionPathsEqual(
            parsed, [
                ('$$Abstract', 1),
            ]
        )

    def test_paper_chem(self):
        parsed = self.get_parsed('10.1016-j.matchemphys.2013.04.003.xml', __file__)

        self.assertJournalEqual(parsed, 'Materials Chemistry and Physics')
        self.assertTitleEqual(
            parsed,
            'Synthesis and characterization of azo benzothiazole chromophore based liquid crystal macromers: '
            'Effects of substituents on benzothiazole ring and terminal group on mesomorphic, '
            'thermal and optical properties')
        self.assertKeywordsEqual(
            parsed, [
                'Liquid crystals',
                'Chemical synthesis',
                'Optical microscopy',
                'Optical properties']
        )
        self.assertSectionPathsEqual(
            parsed, [
                ('$$Abstract', 1),
                ('$$Introduction', 3),
                ('$$Experimental section$$Materials', 1),
                ('$$Experimental section$$Characterization techniques', 1),
                ('$$Experimental section$$Synthesis', 1),
                ('$$Experimental section$$Synthesis'
                 '$$Synthesis of 2-[4′-(6-methacryloyloxyhexyloxy)phenylazo]benzothiazole, (M1)'
                 '$$2-(4′-Hydroxyphenylazo)benzothiazole (1a)', 1),
                ('$$Experimental section$$Synthesis'
                 '$$Synthesis of 2-[4′-(6-methacryloyloxyhexyloxy)phenylazo]benzothiazole, (M1)'
                 '$$2-[4′-(6-Bromohexyloxy)phenylazo]benzothiazole (2a)', 1),
                ('$$Experimental section$$Synthesis'
                 '$$Synthesis of 2-[4′-(6-methacryloyloxyhexyloxy)phenylazo]benzothiazole, (M1)'
                 '$$2-[4′-(6-Methacryloyloxyhexyloxy)phenylazo]benzothiazole, (M1)', 1),
                ('$$Experimental section$$Synthesis'
                 '$$Synthesis of 2-[4′-(6-methacryloyloxyhexyloxy)phenylazo]-6-methylbenzothiazole, (M2)'
                 '$$2-(4′-Hydroxyphenylazo)-6-methyl]benzothiazole (1b)', 1),
                ('$$Experimental section$$Synthesis'
                 '$$Synthesis of 2-[4′-(6-methacryloyloxyhexyloxy)phenylazo]-6-methylbenzothiazole, (M2)'
                 '$$2-[4′-(6-Bromohexyloxy)phenylazo]-6-methylbenzothiazole (2b)', 1),
                ('$$Experimental section$$Synthesis'
                 '$$Synthesis of 2-[4′-(6-methacryloyloxyhexyloxy)phenylazo]-6-methylbenzothiazole, (M2)'
                 '$$2-[4′-(6-Methacryloyloxyhexyloxy)phenylazo]-6-methylbenzothiazole, (M2)', 1),
                ('$$Experimental section$$Synthesis'
                 '$$Synthesis of 2-[4′-(6-methacryloyloxyhexyloxy)phenylazo]-6-methoxybenzothiazole, (M3)'
                 '$$[2-(4′-Hydroxyphenylazo)-6-methoxy]benzothiazole (1c)', 1),
                ('$$Experimental section$$Synthesis'
                 '$$Synthesis of 2-[4′-(6-methacryloyloxyhexyloxy)phenylazo]-6-methoxybenzothiazole, (M3)'
                 '$$2-[4′-(6-Bromohexyloxy)phenylazo]-6-methoxybenzothiazole (2c)', 1),
                ('$$Experimental section$$Synthesis'
                 '$$Synthesis of 2-[4′-(6-methacryloyloxyhexyloxy)phenylazo]-6-methoxybenzothiazole, (M3)'
                 '$$2-[4′-(6-Methacryloyloxyhexyloxy)phenylazo]-6-methoxybenzothiazole, (M3)', 1),
                ('$$Experimental section$$Synthesis'
                 '$$Synthesis of 2-[4′-(6-methacryloyloxyhexyloxy)phenylazo]-6-ethoxybenzothiazole, (M4)'
                 '$$[2-(4′-Hydroxyphenylazo)-6-ethoxy]benzothiazole (1d)', 1),
                ('$$Experimental section$$Synthesis'
                 '$$Synthesis of 2-[4′-(6-methacryloyloxyhexyloxy)phenylazo]-6-ethoxybenzothiazole, (M4)'
                 '$$2-[4′-(6-Bromohexyloxy)phenylazo]-6-ethoxybenzothiazole (2d)', 1),
                ('$$Experimental section$$Synthesis'
                 '$$Synthesis of 2-[4′-(6-methacryloyloxyhexyloxy)phenylazo]-6-ethoxybenzothiazole, (M4)'
                 '$$2-[4′-(6-Methacryloyloxyhexyloxy)phenylazo]-6-ethoxybenzothiazole, (M4)', 1),
                ('$$Results and discussion$$Thermal properties', 2),
                ('$$Results and discussion$$Mesomorphic behaviors', 7),
                ('$$Results and discussion$$Optical properties', 2),
                ('$$Conclusions', 1),
            ]
        )

    def test_paper_with_chemical_formulas(self):
        parsed = self.get_parsed('10.1016-j.materresbull.2015.04.014.xml', __file__)

        self.assertJournalEqual(parsed, 'Materials Research Bulletin')
        self.assertTitleEqual(
            parsed,
            'Electronic structure, optical and thermal/concentration '
            'quenching properties of Lu2−2xEu2xWO6 (0 ≤ x ≤0.2)')
        self.assertKeywordsEqual(
            parsed, [
                'A. Inorganic compounds',
                'B. Luminescence',
                'B. Optical properties',
                'C. XAFS',
                'D. Electronic structure',
            ]
        )
        self.assertSectionPathsEqual(
            parsed, [
                ('$$Abstract', 1),
                ('$$Introduction', 2),
                ('$$Experimental$$Starting materials', 1),
                ('$$Experimental$$Synthesis of Lu2(1−x)Eu2xWO6 (0 ≤ x ≤ 0.20)', 1),
                ('$$Experimental$$Electronic structure calculation', 1),
                ('$$Experimental$$Characterization', 3),
                ('$$Results and discussion'
                 '$$Electronic structure and optical properties of Lu2(1−x)Eu2xWO6 (x = 0, 0.1)', 3),
                ('$$Results and discussion'
                 '$$Valency state and coordination number of Eu ion in Lu1.8Eu0.2WO6', 1),
                ('$$Results and discussion'
                 '$$Thermal quenching mechanism of Lu1.8Eu0.2WO6', 1),
                ('$$Results and discussion'
                 '$$Concentration mechanism of Lu2−2xEu2xWO6 (0.05 ≤ x ≤0.2)', 1),
                ('$$Conclusions', 1),
            ]
        )
        self.assertMaterialMentioned(
            parsed,
            ['Lu2WO6', 'Lu2(1−x)Eu2xWO6', 'Lu1.8Eu0.2WO6', 'CdWO4'],
            ['Lu2WO6 ']
        )