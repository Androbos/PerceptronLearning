# PerceptronLearning
Implementation of Perceptron Learning Rule in python, consult README.md for detail


Perceptron training rule with a simple weight-update scheme:

    w' ← w +∆w
where
    ∆w = η (t−o) xi

Where:
    xi is a random sample from the testcases
    t = c(x) is target value
    o is perceptron output
    η is a small constant called learning rate
    between 0 and 1
    to simplify things you may assume η = 1
    but in practice usually set at less than 0.2, e.g., 0.1 η can be varied during learning