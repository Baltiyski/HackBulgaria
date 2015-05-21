def loss_or_profit(income, outcome):
    countForIncome = 0;
    countForOutcome = 0;

    for inc in income:
        countForIncome += inc;

    for out in outcome:
        countForOutcome += out;

    count = countForIncome - countForOutcome;

    return count;


print(loss_or_profit([1,2,3],[3]));
print(loss_or_profit([10],[20, 30]));
print(loss_or_profit([10],[10]));
