

class BaseTester:

    @staticmethod
    def run_test(function, parameter, expected):
        result = function(parameter)
        result_str = str(parameter) + ": " + str(expected) + " --> " + str(result) + ": "
        try:
            assert expected == result
            result_str += "Passed"
        except AssertionError as e:
            result_str += "Failed"

        return result_str, "Passed" in result_str

    @staticmethod
    def run_test_multi(function, parameters, expected):
        result = function(*parameters)
        param_str = [[str(param)] for param in parameters]
        result_str = str(param_str) + ": " + str(expected) + " --> " + str(result) + ": "
        try:
            assert expected == result
            result_str += "Passed"
        except AssertionError as e:
            result_str += "Failed"

        return result_str, "Passed" in result_str

    @staticmethod
    def test_all(function, inputs, outputs, verbose=False):
        passed_count = 0
        out_str = ""
        for i in range(len(inputs)):
            result, passed = BaseTester.run_test(function, inputs[i], outputs[i])
            out_str += (f"Test: {i + 1} - {function.__name__}: " + result) + "\n"
            if passed:
                passed_count += 1

        return BaseTester.print_results(function, out_str, passed_count, len(inputs), verbose)

    @staticmethod
    def test_all_multi_param(function, inputs, outputs, verbose=False):
        passed_count = 0
        out_str = ""
        for i in range(len(inputs[0])):
            parameters = list()
            for j in range(len(inputs)):
                parameters.append(inputs[j][i])

            result, passed = BaseTester.run_test_multi(function, parameters, outputs[i])
            out_str += (f"Test: {i + 1} - {function.__name__}: " + result) + "\n"
            if passed:
                passed_count += 1

        return BaseTester.print_results(function, out_str, passed_count, len(inputs[0]), verbose)

    @staticmethod
    def print_results(function, out_str, passed_count, num_tests, verbose=False):
        if verbose or passed_count < num_tests:
            print(out_str.rstrip())

        if passed_count == num_tests:
            print(f"{function.__name__} - All Tests Passed")
            return True
        else:
            print(f"{function.__name__} - {passed_count} of {num_tests} Passed")
            return False
