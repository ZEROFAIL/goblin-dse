import goblin_dse


def test_get_id_hash():
    distinct_ids = (
        {"~label": "label1", "community_id": 6335574440, "member_id": 1},
        {"~label": "label1", "community_id": 6335574440, "member_id": 2},
        {"~label": "label1", "community_id": 8412991644, "member_id": 1},
        {"~label": "label2", "community_id": 6335574440, "member_id": 1},
        {"~label": "vertex_with_custom_id",
         "custom_partition_key_name": "custom_partition_key_value"},
    )

    same_ids = (
        {"~label": "label1", "community_id": 6335574440, "member_id": 1},
        {"~label": "label1", "community_id": 6335574440, "member_id": 1},
    )

    distinct_id_hashes_set = {goblin_dse.dse_get_hashable_id(val) for val in distinct_ids}
    same_ids_hashes_set = {goblin_dse.dse_get_hashable_id(val) for val in same_ids}

    assert len(distinct_id_hashes_set) == len(distinct_ids)
    assert len(same_ids_hashes_set) == 1
