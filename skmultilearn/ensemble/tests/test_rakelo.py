import unittest

from skmultilearn.ensemble.rakelo import RakelO
from skmultilearn.meta.lp import LabelPowerset
from skmultilearn.tests.classifier_basetest import ClassifierBaseTest
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import make_multilabel_classification
from sklearn.cross_validation import train_test_split
from sklearn.utils.estimator_checks import check_estimator

class RakelOTest(ClassifierBaseTest):
    def get_labelpowerset_with_svc(self):
        return LabelPowerset(classifier = SVC(), require_dense = [False, True])

    def get_labelpowerset_with_nb(self):
        return LabelPowerset(classifier = GaussianNB(), require_dense = [True, True])


    def test_if_sparse_classification_works_on_non_dense_base_classifier(self):
        classifier = RakelO(classifier = self.get_labelpowerset_with_svc(), models = 20, labelset_size = 5)

        self.assertClassifierWorksWithSparsity(classifier, 'sparse')

    def test_if_dense_classification_works_on_non_dense_base_classifier(self):
        classifier = RakelO(classifier = self.get_labelpowerset_with_svc(), models = 20, labelset_size = 5)

        self.assertClassifierWorksWithSparsity(classifier, 'dense')

    def test_if_sparse_classification_works_on_dense_base_classifier(self):
        classifier = RakelO(classifier = self.get_labelpowerset_with_nb(), models = 20, labelset_size = 5)

        self.assertClassifierWorksWithSparsity(classifier, 'sparse')

    def test_if_dense_classification_works_on_dense_base_classifier(self):
        classifier = RakelO(classifier = self.get_labelpowerset_with_nb(), models = 20, labelset_size = 5)

        self.assertClassifierWorksWithSparsity(classifier, 'dense')

if __name__ == '__main__':
    unittest.main()