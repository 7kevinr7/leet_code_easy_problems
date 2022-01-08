
class BaseTester:

    @staticmethod
    def run_test(test_num, function, values, expected):
        result = function(values)
        print(f"Test {test_num} - {values}: {expected} -> {result}")
        assert expected == result

    @staticmethod
    def run_test_multi_param(test_num, function, values, expected):
        result = function(*values)
        print(f"Test {test_num} - {values}: {expected} -> {result}")
        assert expected == result

    @staticmethod
    def test_all(function, inputs, outputs):
        print(f"{function.__name__}:")
        for i in range(len(inputs)):
            BaseTester.run_test(i + 1, function, inputs[i], outputs[i])

    @staticmethod
    def test_all_multi_param(function, inputs, outputs):
        print(f"{function.__name__}:")

        for i in range(len(inputs[0])):
            parameters = list()
            for j in range(len(inputs)):
                parameters.append(inputs[j][i])

            BaseTester.run_test_multi_param(i + 1, function, parameters, outputs[i])
