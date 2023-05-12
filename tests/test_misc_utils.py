
import numpy as np

from src.ossr_utils.misc_utils import get_colors, get_dists, logsumexp, get_majority_str, gauss_pdf


def test_get_colors():
    n = 50
    colors = get_colors(n)
    assert colors.shape == (n, 3)

def test_get_dists():
    M = 2
    N = 3
    D = 4
    X = np.random.randn(M, D)
    Y = np.random.randn(N, D)
    dists = get_dists(X, Y)
    i, j = 0, 1

    assert dists.shape == (M, N)
    assert np.sqrt(np.sum((X[i, :] - Y[j, :]) ** 2)) == dists[i, j]

def test_logsumexp():
    x = np.array([[-2, 3.1, 5], [0.3, 1.05, -5]])
    y = logsumexp(x, axis=1)

    y_expected = np.array([[5.14017968], [1.43847113]])

    assert np.allclose(y, y_expected)

def test_get_majority_string():
    strs1 = ['a', 'b', 'a', 'e', 'y', 'b', 'a', '0', 'asdfasdf'] # clear majority
    out = get_majority_str(strs1)
    assert out == 'a'

    strs1 = ['b', 'a', 'a', 'e', 'y', 'b', 'a', '0', 'b', 'asdfasdf'] # tie between 'a' and 'b'
    out = get_majority_str(strs1)
    assert out == 'a'

def test_gauss_pdf():
    mu = 2
    var = 1
    x = np.linspace(-1, 5, 5)
    y = gauss_pdf(mu, var, x, include_norm=True, wrap=[0, 4])
    y_expected = np.array([0.24640406, 0.147046, 0.39920994, 0.147046, 0.24640406])
    assert np.allclose(y, y_expected)





if __name__ == "__main__":
    test_get_colors()
    test_get_dists()
    test_logsumexp()
    test_get_majority_string()
    test_gauss_pdf()