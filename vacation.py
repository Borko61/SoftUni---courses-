needed_money = float(input())
money_at_the_moment = float(input())
is_money_saved = False
money_after_spend_or_save = money_at_the_moment
days_spend = 0
all_days = 0
while True:
    if days_spend >= 5:
        break

    money_movement = input()
    sum = float(input())
    all_days += 1

    if money_movement == 'spend':
        money_after_spend_or_save -= sum
        if money_after_spend_or_save < 0:
            money_after_spend_or_save = 0
        days_spend += 1


    elif money_movement == 'save':
        money_after_spend_or_save += sum
        days_spend = 0
    if money_after_spend_or_save >= needed_money:
        is_money_saved = True
        break

if days_spend >= 5:
    print(f"You can't save the money.")
    print(all_days)
elif money_after_spend_or_save >= needed_money:
    print(f'You saved the money for {all_days} days.')