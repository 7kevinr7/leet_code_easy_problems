
import src.avg_bt_levels as avg_bt_levels
import src.binary_search as binary_search
import src.buy_sell_stock as buy_sell_stock
import src.climbing_stairs as climbing_stairs
import src.contains_duplicate as contains_duplicate
import src.counting_bits as counting_bits
import src.diameter_bt as diameter_bt
import src.lca_bst as lca_bst
import src.linked_list_cycle as linked_list_cycle
import src.max_depth_bt as max_depth_bt
import src.max_subarray as max_subarray
import src.merge_bt as merge_bt
import src.merge_sorted_lists as merge_sorted_lists
import src.middle_linked_list as middle_linked_list
import src.min_depth_bt as min_depth_bt
import src.missing_number as missing_number
import src.next_greatest_letter as next_greatest_letter
import src.numbers_disappeared_in_array as numbers_disappeared_in_array
import src.palindrome_linked_list as palindrome_linked_list
import src.path_sum as path_sum
import src.peak_index_mt_array as peak_index
import src.remove_duplicates_list as rm_duplicates_list
import src.remove_linked_list as remove_linked_list
import src.reverse_linked_list as reverse_linked_list
import src.same_tree as same_tree
import src.single_number as single_number
import src.subtree_another_tree as subtree_another_tree
import src.range_sum_query as sum_query
from sys import argv


def main():

    verbose = False
    run_all = False

    if "verbose=True" in argv:
        verbose = True
    if "run_all=True" in argv:
        run_all = True

    if run_all:
        avg_bt_levels.Tester.test(verbose)
        binary_search.Tester.test(verbose)
        buy_sell_stock.Tester.test(verbose)
        climbing_stairs.Tester.test(verbose)
        contains_duplicate.Tester.test(verbose)
        counting_bits.Tester.test(verbose)
        linked_list_cycle.Tester.test(verbose)
        max_subarray.Tester.test(verbose)
        merge_sorted_lists.Tester.test(verbose)
        middle_linked_list.Tester.test(verbose)
        min_depth_bt.Tester.test(verbose)
        missing_number.Tester.test(verbose)
        next_greatest_letter.Tester.test(verbose)
        numbers_disappeared_in_array.Tester.test(verbose)
        palindrome_linked_list.Tester.test(verbose)
        peak_index.Tester.test(verbose)
        rm_duplicates_list.Tester.test(verbose)
        remove_linked_list.Tester.test(verbose)
        reverse_linked_list.Tester.test(verbose)
        single_number.Tester.test(verbose)
        sum_query.Tester.test(verbose)
        same_tree.Tester.test(verbose)
        path_sum.Tester.test(verbose)
        max_depth_bt.Tester.test(verbose)
        diameter_bt.Tester.test(verbose)
        merge_bt.Tester.test(verbose)
        lca_bst.Tester.test(verbose)

    subtree_another_tree.Tester.test()


if __name__ == '__main__':
    main()
