import pickle

# TODO:
# How to see which item in outputs didnt't match?
# Display associated input with output failures.
# Make it so you can't record and approve at same time (this will always pass)
# Will probably want to extract list comparison tool so can use it to write the
#   custom assertion that goes in.
# Efficiently handle very long lists of inputs
# Create class and extract file names and func,
#   file_prefix and func can be passed into ctor

def record(func, inputs, file_prefix='an_approval_test'):
    inputs_filename = '{}_inputs.pickle'.format(file_prefix)
    with open(inputs_filename, 'w') as inputs_file:
        pickle.dump(inputs, inputs_file)

    outputs = [func(i) for i in inputs]

    expected_outputs_filename = '{}_expected_outputs.pickle'.format(
        file_prefix
    )
    with open(expected_outputs_filename, 'w') as expected_outputs_file:
        pickle.dump(outputs, expected_outputs_file)


def approve(func, comp, file_prefix='an_approval_test'):
    inputs_filename = '{}_inputs.pickle'.format(file_prefix)
    with open(inputs_filename, 'r') as inputs_file:
        inputs = pickle.load(inputs_file)

    outputs = [func(i) for i in inputs]

    expected_outputs_filename = '{}_expected_outputs.pickle'.format(
        file_prefix
    )
    with open(expected_outputs_filename, 'r') as expected_outputs_file:
        expected_outputs = pickle.load(expected_outputs_file)
    all(comp(x[0], x[1]) for x in zip(expected_outputs, outputs))