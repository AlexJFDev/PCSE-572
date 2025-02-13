# Analyze Lie ("Lee") Brackets using Symbolic Python
# This is some starter code you might use if you don't have Mathematica

from sympy import symbols, cos, sin, simplify, Matrix
from sympy import init_printing

# Enable pretty printing
init_printing( use_unicode=True)


def show_matrix(mat):
    """
    Display matrix in a prettier view
    """
    matrix_list = mat.T.tolist()
    # Determine the maximum width needed for any element
    max_widths_per_column = [max([len(str(element)) for element in col]) for col in matrix_list ]

    matrix_list = mat.tolist()
    format_strings = [f'  {{:>{w}}}  ' for w in max_widths_per_column]
    fmt_string = "| " + " ".join(format_strings) + " |"
    for row in matrix_list:
        # for item in row:
        #     print(item, type(item))
        print(fmt_string.format(*[str(item) for item in row]))
    print()

if __name__ == '__main__':

    print("Lie Bracket analysis of diff-drive towing a trailer:")
    # Define symbols
    configuration = symbols('x y theta phi')
    L = symbols('L')  # parameter

    x, y, theta, phi = configuration
    print("configuration=", configuration)

    g1 = Matrix([cos(theta), sin(theta), 0, -sin(phi)/L])

    print('g1=')
    show_matrix(g1)

    dg1dq = simplify(g1.jacobian(configuration))
    print("dg1/dq = ")
    show_matrix(dg1dq)
