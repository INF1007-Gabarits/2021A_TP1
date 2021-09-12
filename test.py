from exercice1 import calculerEnergie
from exercice3 import resoudreEquation
from exercice3 import calculerNombreChiffres
from exercice4 import decomposer
from exercice7 import trouverModule
from exercice7 import effectuerRotation
import numpy as np
from random import randint
import unittest
import os
import sys

class TestExercice1(unittest.TestCase):
    CONST_SIZE = 10
    def test_calculerEnergie(self):
        array = np.random.randint(0,1000, size=(self.CONST_SIZE, 2))
        for masse, vitesse in array:
            self.assertAlmostEqual(calculerEnergie(masse, vitesse), 0.5 * masse * ((vitesse/3.6) ** 2))

class TestExercice2(unittest.TestCase):
    def test_no_solution(self):
        self.assertEqual(resoudreEquation(1,1,1), None)
    def test_one_solution(self):
        a, b, c = 1,-2,1
        expectedSolution = 1
        self.assertEqual(resoudreEquation(a, b, c), expectedSolution)
    def test_two_solutions(self):
        a, b, c = 1, -4, 3
        x1, x2 = 1, 3
        b1 = resoudreEquation(a, b, c)[0] == x1 and resoudreEquation(a, b, c)[1] == x2
        b2 = resoudreEquation(a, b, c)[0] == x2 and resoudreEquation(a, b, c)[1] == x1
        self.assertTrue(b1 or b2)

class TestExercise3(unittest.TestCase):
    def test_chiffres(self):
        for i in range(1,10):
            number = np.random.randint(10**(i-1), 10**i-1)
            self.assertEqual(calculerNombreChiffres(number), i)

class TestExercise4(unittest.TestCase):
    CONST_UNE_ANNEE = 3600 * 24 * 365
    CONST_UNE_SEMAINE = 3600 * 24 * 7
    CONST_UN_JOUR = 3600 * 24
    CONST_UNE_HEURE = 3600
    CONST_UNE_MINUTE = 60
    def test_complet(self):
        annees, semaines, jours, heures, minutes, secondes = 3, 3, 4, 5, 34, 9
        secondesTotal = self.calculerSecondes(annees, semaines, jours, heures, minutes, secondes)
        self.assertEqual(decomposer(secondesTotal), (annees, semaines, jours, heures, minutes, secondes))
    def test_semaines(self):
        annees, semaines, jours, heures, minutes, secondes = 0, 3, 4, 5, 34, 9
        secondesTotal = self.calculerSecondes(annees, semaines, jours, heures, minutes, secondes)
        self.assertEqual(decomposer(secondesTotal), (annees, semaines, jours, heures, minutes, secondes))
    def test_jours(self):
        annees, semaines, jours, heures, minutes, secondes = 0, 0, 4, 5, 34, 9
        secondesTotal = self.calculerSecondes(annees, semaines, jours, heures, minutes, secondes)
        self.assertEqual(decomposer(secondesTotal), (annees, semaines, jours, heures, minutes, secondes))
    def test_heures(self):
        annees, semaines, jours, heures, minutes, secondes = 0, 0, 0, 5, 34, 9
        secondesTotal = self.calculerSecondes(annees, semaines, jours, heures, minutes, secondes)
        self.assertEqual(decomposer(secondesTotal), (annees, semaines, jours, heures, minutes, secondes))
    def test_minutes(self):
        annees, semaines, jours, heures, minutes, secondes = 0, 0, 0, 0, 34, 9
        secondesTotal = self.calculerSecondes(annees, semaines, jours, heures, minutes, secondes)
        self.assertEqual(decomposer(secondesTotal), (annees, semaines, jours, heures, minutes, secondes))
    def test_secondes(self):
        annees, semaines, jours, heures, minutes, secondes = 0, 0, 0, 0, 0, 9
        secondesTotal = self.calculerSecondes(annees, semaines, jours, heures, minutes, secondes)
        self.assertEqual(decomposer(secondesTotal), (annees, semaines, jours, heures, minutes, secondes))

    def calculerSecondes(self, annees, semaines, jours, heures, minutes, secondes):
        return annees * self.CONST_UNE_ANNEE + semaines * self.CONST_UNE_SEMAINE + \
               jours * self.CONST_UN_JOUR + heures * self.CONST_UNE_HEURE + \
               minutes * self.CONST_UNE_MINUTE + secondes


class TestExercice5(unittest.TestCase):
    CONST_SIZE = 50
    def test_trouverModule(self):
        RandomListOfComplex = [self.genererComplexeAleatoire() for iter in range(self.CONST_SIZE)]
        for number in RandomListOfComplex:
            self.assertAlmostEqual(abs(number), trouverModule(number))

    def test_effectuerRotation(self):
        RandomListOfComplex = [self.genererComplexeAleatoire() for iter in range(self.CONST_SIZE)]

        for number in RandomListOfComplex:
            rotation = self.genererAngleAleatoire()
            result = effectuerRotation(number, rotation, abs)
            self.assertAlmostEqual(self.trouverAngle(result), self.angleApresRotation(self.trouverAngle(number), rotation))
            self.assertAlmostEqual(abs(number), abs(result), 3)

    def angleApresRotation(self, angle, rotation):
        resultat = angle + rotation
        if abs(resultat) > 180:
            return resultat - 360 if resultat > 0 else resultat + 360
        return resultat

    def trouverAngle(self, nombre):
        return np.angle(nombre, deg= True)

    def genererComplexeAleatoire(self):
        return complex(randint(-5000, 5000), randint(-5000, 5000))

    def genererAngleAleatoire(self):
        return randint(-360, 360)


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
