import pytest

from src.blazefl.utils import FilteredDataset


def test_filtered_dataset_basic() -> None:
    original_data = [0, 1, 2, 3, 4]
    original_targets = [10, 11, 12, 13, 14]
    indices = [1, 3]

    dataset = FilteredDataset(indices, original_data, original_targets)
    assert len(dataset) == 2

    data, target = dataset[0]
    assert data == 1
    assert target == 11

    data, target = dataset[1]
    assert data == 3
    assert target == 13


def test_filtered_dataset_no_targets() -> None:
    original_data = ["img1", "img2", "img3"]
    indices = [0, 2]

    dataset = FilteredDataset(indices, original_data)
    assert len(dataset) == 2

    data = dataset[0]
    assert data == "img1"
    data = dataset[1]
    assert data == "img3"


def test_filtered_dataset_transform() -> None:
    original_data = [1, 2, 3]
    original_targets = [4, 5, 6]
    indices = [0, 1]

    def transform(x):
        return x * 2

    def target_transform(x):
        return x + 10

    dataset = FilteredDataset(
        indices,
        original_data,
        original_targets,
        transform=transform,
        target_transform=target_transform,
    )

    data, target = dataset[0]
    assert data == 2
    assert target == 14


def test_filtered_dataset_assert_length_mismatch() -> None:
    original_data = [0, 1, 2]
    original_targets = [10, 11]  # Length mismatch

    indices = [0, 1]
    with pytest.raises(AssertionError):
        _ = FilteredDataset(indices, original_data, original_targets)


def test_filtered_dataset_empty_indices() -> None:
    original_data = [0, 1, 2]
    original_targets = [10, 11, 12]
    indices = []  # Empty indices

    dataset = FilteredDataset(indices, original_data, original_targets)
    assert len(dataset) == 0
    with pytest.raises(IndexError):
        _ = dataset[0]
