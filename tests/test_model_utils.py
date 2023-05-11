
import numpy as np

from src.model_utils import get_conf_mat


def test_get_conf_mat():
    tags_train = ['a', 'c', 'dd', '345', 'asfa_@#']
    tags_test = ['545', 'c', 'dd', 'asdsfsd']
    tags_test_true = ['545', '545', 'c', 'dd', 'c']
    tags_test_pred = ['345', 'c', 'c', 'dd', 'c']
    normalize = False

    conf_mat = get_conf_mat(tags_train, tags_test, tags_test_true, tags_test_pred, normalize=normalize)

    conf_mat_expected = np.array(
        [[0, 0, 0, 0],
         [1, 2, 0, 0],
         [0, 0, 1, 0],
         [1, 0, 0, 0],
         [0, 0, 0, 0]]
    )

    assert np.allclose(conf_mat, conf_mat_expected)






if __name__ == "__main__":
    test_get_conf_mat()