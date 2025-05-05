import numpy as np

def calculate(input_list):
    """
    Given a list of 9 numbers, returns a dict with:
      - 'mean': [col_means, row_means, overall_mean]
      - 'variance': [col_vars, row_vars, overall_var]
      - 'standard deviation': [col_stds, row_stds, overall_std]
    """
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(input_list).reshape(3, 3)

    result = {
        'mean': [
            list(arr.mean(axis=0)),
            list(arr.mean(axis=1)),
            float(arr.mean())
        ],
        'variance': [
            list(arr.var(axis=0)),
            list(arr.var(axis=1)),
            float(arr.var())
        ],
        'standard deviation': [
            list(arr.std(axis=0)),
            list(arr.std(axis=1)),
            float(arr.std())
        ]
    }
    return result

# Example usage
if __name__ == '__main__':
    data = [0,1,2,3,4,5,6,7,8]
    print(calculate(data))
