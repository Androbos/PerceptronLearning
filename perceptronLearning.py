#!/usr/bin/python

import ast
import re
import numpy as np

# perceptron learning
# starting weights 1

def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    return 0


class perceptronLearning(object):

    Feature_Regex = "Features\s*=\s*(\d+)\s*;"
    TrainingData_Regex = "TrainingData\s*=\s*(\[[\-01\s\,\[\]]+\])\s*;"
    TargetValue_Regex = "TargetValue\s*=\s*(\[[1\-\,\s]+\])\s*;"

    def __init__(self, num_feature=None):
        super(perceptronLearning, self).__init__()
        self.num_features = num_feature
        self.trainingData = None
        self.targetValues = None
        self.weights = None
        self.learningRate = 0.7

    def load_training_data_from_file(self, fn_in):
        assert type(fn_in) is str, "fn_in must be strings: %r" % fn_in
        f_in = open(fn_in, "r")
        # f_out = open(fn_out, "w")
        # f_detail = open(fn_detail, "w")

        temp = list(f_in)
        (featureline, trainingDataLine, targetValueline) = [x.rstrip() for x in temp]

        m = re.search(perceptronLearning.Feature_Regex, featureline)
        if m:
            self.num_features = int(m.group(1))
        else:
            print featureline
            raise Exception("Wrong File Format", "File format for Feature Line Wrong")

        m = re.search(perceptronLearning.TrainingData_Regex, trainingDataLine)
        if m:
            self.trainingData = ast.literal_eval(m.group(1))
        else:
            print trainingDataLine
            raise Exception("Wrong File Format", "File format for trainingData Line Wrong")

        m = re.search(perceptronLearning.TargetValue_Regex, targetValueline)
        if m:
            self.targetValues = ast.literal_eval(m.group(1))
        else:
            print targetValueline
            raise Exception("Wrong File Format", "File format for targetValue Line Wrong")

        # print num_feature
        # print trainingData
        # print targetValues

    def add_training_example(self, num_feature, trainingData, targetValue):
        assert(num_feature == self.num_features or self.num_features is None), "wrong number of features"
        assert(len(trainingData) == num_feature), "number of features in trainingData doesn't match num_feature"
        assert(targetValue == -1 or targetValue == 1), "concept value must equal to 0 or 1"
        self.num_features = num_feature

        if type(self.trainingData) is None:
            self.trainingData = list()
        if type(self.targetValues) is None:
            self.targetValues = list()

        self.trainingData.append(list(trainingData))
        self.targetValues.append(targetValue)

<<<<<<< HEAD
    def runAlgorithm(self):
        weights = np.ones(self.num_features+1)
=======
    def genWeights(self):
        weights = np.zeros(self.num_features+1)
>>>>>>> d31f189b5283c89202796ab4f8b492060d064f4b

        trainingSets = [np.array([1]+x) for x in self.trainingData]

        trainSets = np.array(zip(trainingSets, self.targetValues))

        notConverge = True

        while notConverge:
            notConverge = False
            for testcase, targetVal in trainSets:
                c = sign(sum(weights*testcase))
                if c*targetVal <= 0:
                    weights += self.learningRate * (targetVal - c) * testcase
                    notConverge = True

        self.weights = list(weights)

    # return 1 for accepted test case
    # return -1 for rejected test case
    # return 0 for undecidable
    def predict(self, input_TestCase):
        assert(len(input_TestCase) == self.num_features or self.num_features is not None), "wrong number of features"

        new_testCase = np.array([1] + input_TestCase)

        return sign(sum(self.weights * new_testCase))
