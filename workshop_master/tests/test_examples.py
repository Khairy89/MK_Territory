EXPECTED = 'Hello Larry my name is Mary'


def test_01():
    from workshop_master.fortytwo.s01_find_action import main
    assert EXPECTED == main()


def test_02():
    from workshop_master.fortytwo.s02_reduce_clutter import main
    assert EXPECTED == main()


def test_03():
    from workshop_master.fortytwo.s03_disable_tabs import main
    assert EXPECTED == main()


def test_04():
    from workshop_master.fortytwo.s04_recent_file import main
    assert EXPECTED == main()


def test_05():
    from workshop_master.fortytwo.s05_recent_tool import main
    assert EXPECTED == main()


def test_06():
    from workshop_master.fortytwo.s06_navigate_symbol import main
    assert EXPECTED == main()


def test_07():
    from workshop_master.fortytwo.s07_navigate_file import main
    assert EXPECTED == main()


def test_08():
    from workshop_master.fortytwo.s08_navigate_cursor import main
    assert EXPECTED == main()


def test_09():
    from workshop_master.fortytwo.s09_activate_navbar import main
    assert EXPECTED == main()


def test_09():
    from workshop_master.fortytwo.s09_activate_navbar import main
    assert EXPECTED == main()


def test_10():
    from workshop_master.fortytwo.s10_navigate_files_navbar import main
    assert EXPECTED == main()


def test_11():
    from workshop_master.fortytwo.s11_open_file_navbar import main
    assert EXPECTED == main()


def test_12():
    from workshop_master.fortytwo.s12_speedsearch_navbar import main
    assert EXPECTED == main()


def test_13():
    from workshop_master.fortytwo.s13_create_file_navbar import main
    assert EXPECTED == main()


def test_14():
    from workshop_master.fortytwo.s14_find_in_path_navbar import main
    assert EXPECTED == main()


def test_15():
    from workshop_master.fortytwo.s15_add_line import main
    assert EXPECTED == main()


def test_16():
    from workshop_master.fortytwo.s16_make_extend_selection import main
    assert EXPECTED == main()


def test_17():
    from workshop_master.fortytwo.s17_move_block import main
    assert EXPECTED == main()


def test_18():
    from workshop_master.fortytwo.s18_reformat_code import main
    assert EXPECTED == main()


def test_19():
    from workshop_master.fortytwo.s19_optimize_imports import main
    assert EXPECTED == main()


def test_20():
    from workshop_master.fortytwo.s20_generate_imports import main
    assert EXPECTED == main()


def test_21():
    from workshop_master.fortytwo.s21_install_and_import import main
    assert 'Mary' in main()


def test_22():
    from workshop_master.fortytwo.s22_adding_fields import main
    assert EXPECTED == main()


def test_23():
    from workshop_master.fortytwo.s23_rename_file import main
    assert EXPECTED == main()


def test_24():
    from workshop_master.fortytwo.s24_rename_symbol import main
    assert EXPECTED == main()


def test_27():
    from workshop_master.fortytwo.s27_run_from_keyboard import main
    assert EXPECTED == main()


def test_28():
    from workshop_master.fortytwo.s28_conditional_breakpoints import main
    assert 'Mary' in main()


def test_29():
    from workshop_master.fortytwo.s29_evaluate_expression import main
    assert 'Mary' in main()


def test_30():
    from workshop_master.fortytwo.s30_split_screen import main
    assert EXPECTED == main()


def test_31():
    from workshop_master.fortytwo.s31_run_single_test import main
    assert EXPECTED == main()


def test_32():
    from workshop_master.fortytwo.s32_autorun_tests import main
    assert EXPECTED == main()


def test_33():
    from workshop_master.fortytwo.s33_spot_coverage_gaps_in_gutter import main
    assert EXPECTED == main()

# def test_3():
#     from workshop_master.fortytwo.s3 import main
#     assert EXPECTED == main()
#
