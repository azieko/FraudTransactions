#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detecting fraudulent credit card transactions"""

__author__ = "Azieko"

from collections import namedtuple
import statistics

Transaction = namedtuple("Transaction", ["time", "amount", "company", "phone"])


def foreign_transactions(transactions):
    """Return a list of foreign transactions."""
    foreign = []
    for ele in transactions:
        if ele.phone.find("+1") == -1:
            foreign.append(ele)
    return foreign


def late_night_transactions(transactions):
    """Return a list of transactions between 11:00 PM - 5:00 AM."""
    """ I DO NOT KNOW WHAT IS WRONG WITH THIS FUNCTION"""
    late = []
    for ele in transactions:
        time = ele.time.split(" ")[1]
        hours, minutes, seconds = time.split(":")
        time = (int(hours)*60) + int(minutes) + (int(seconds)/60)
        start = 1380
        end = 300
        if time >= start or time <= end:
            late.append(ele)
    return late


def highest_transactions(transactions, n_highest=10):
    """Return a list of the n highest transactions."""
    """ not arranged in correct order"""
    highest = []
    lst = []
    for ele in transactions:
        amount = str(ele.amount).replace("$", "")
        lst.append(float(amount))
    lst = sorted(lst, reverse=True)
    lst2 = lst[0: (n_highest)]
    for ele in transactions:
        for x in lst2:
            if x == ele.amount:
                highest.append(ele)
    """ i don't know how to rearrange this according to amount and not year"""
    for ele in transactions:
        highest = sorted(highest, reverse=True)
    return highest


def median_expense(transactions):
    """Return the median value of transaction amounts."""
    val = []
    for ele in transactions:
        val.append(ele.amount)
    return statistics.median(val)


def significant_transactions(transactions, n_trailing=10):
    """Return a list of significant transactions.

    A transaction is significant if the amount is greater than or equal to
    five times of the median spending for a trailing number of transactions
    """
    """ I don't understand the role of trailign transactions in this"""
    # list of values
    val = []
    for ele in transactions:
        val.append(ele.amount)
    sig = []
    start = n_trailing
    i = 0
    T = transactions[n_trailing:]
    for ele in T:
        val1 = val[i:start]
        med = statistics.median(val1)
        if ele.amount >= (5*med):
            sig.append(ele)
        start += 1
        i += 1
    return sig


def fraudulent_transactions(transactions):
    """Return a list of potential fraudulent transactions.
    A transaction is potentially fraudulent if all is true:
        - it is a foreign transaction
        - it happens during late night (11 PM - 5 AM)
        - it is among the top 10 highest transactions
        - significant (using 10 trailing transactions)
    """
    F = foreign_transactions(transactions)
    L = late_night_transactions(transactions)
    S = significant_transactions(transactions)
    H = highest_transactions(transactions)
    final = list(set(F) & set(L) & set(S) & set(H))
    return final


def load_transactions(filename):
    """
    Load credit card transactions from 'filename'.

    Return a list of Transaction objects
    """
    transaction = []
    with open(filename) as db:
        for line in db:
            # line is a single string of from the file
            T = line.strip().split(" | ")
            amount = T[1].replace("$", "")
            T[1] = float(amount)
            T = Transaction(T[0], T[1], T[2], T[3])
            transaction.append(T)
    return transaction


if __name__ == "__main__":
    transactions = load_transactions("transactions.txt")
    # print(highest_transactions(transactions,5))
    # print()

    # print(foreign_transactions(transactions))
    # print(late_night_transactions(transactions))
    # print(highest_transactions(transactions))
    # print(median_expense(transactions))
    # print(significant_transactions(transactions))
    # print(fraudulent_transactions(transactions))
