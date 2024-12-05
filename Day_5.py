import inputs

now_ordered_updates = []


def recheck_order(update, rules):
    for page in update:
        for rule in rules:
            if page == rule[0]:
                if rule[1] in update[:update.index(page):]:
                    order_update(update, rule, rules)
    return True


def order_update(unordered_update, violated_rule, rules):
    index_of_page_to_go_first = unordered_update.index(violated_rule[0])
    index_of_page_to_go_after = unordered_update.index(violated_rule[1])
    del unordered_update[index_of_page_to_go_first]
    unordered_update.insert(index_of_page_to_go_after, violated_rule[0])
    ordered_update = recheck_order(unordered_update, rules)
    if ordered_update is True:
        if unordered_update not in now_ordered_updates:
            now_ordered_updates.append(unordered_update)
    else:
        order_update(unordered_update, ordered_update, rules)


def check_order(update, rules):
    for page in update:
        for rule in rules:
            if page == rule[0]:
                if rule[1] in update[:update.index(page):]:
                    return rule
    return True


def find_sum_of_middle_pages(updates):
    middle_pages = [int(update[int(len(update) / 2)]) for update in updates if update is not None]
    return sum(middle_pages)


def get_middle_page_numbers(data):
    page_order_rules = [rule.split('|') for rule in data.split() if '|' in rule]  # parse out ordering rules
    updates = [update.split(',') for update in data.split() if '|' not in update]  # parse out updates
    ordered_updates = []

    for update in updates:
        result = check_order(update, page_order_rules)
        if result is True:
            ordered_updates.append(update)
        else:
            order_update(update, result, page_order_rules)

    print(f' The sum of the middle pages from the ordered updates is '
          f'{find_sum_of_middle_pages(ordered_updates)}')
    print(f' The sum of the middle pages from the unordered updates is '
          f'{find_sum_of_middle_pages(now_ordered_updates)}')


get_middle_page_numbers(inputs.day_5_data)

