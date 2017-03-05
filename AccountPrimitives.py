from datetime import datetime
from enum import Enum

## ENUMS
class TransactionTypes(Enum):
  incoming= 0
  fees = 1
  food = 2
  clothes = 3
  IT = 4
  withdrawal = 5
  deposit = 6
  culture = 7
  entertainment = 8
  other = 9
  init = 99

class AccountTypes(Enum):
  MAIN = 0
  CARD = 1
  CASH = 2
  init = 99

## CLASSES
class Modification:
  change = 0.0
  ''' value of the changing :type: float'''
  reason = ''
  ''' reason of the modification; :type: string'''
  time_stamp = None
  ''' time point of modification; :type: datetime.datetime'''
  modification_type = None
  ''' class of modification. This field sorts the transaction into a larger group of modifications. For example this money was spend for food, clothes etc.
  :type: TransactionTypes enum'''
  note = ''
  ''' some important information about the modification; :type: string'''


class Account:
  name = ''
  ''' name of the account; :type: string'''
  note = ''
  ''' some important information about the account; :type: string'''
  modification_list = []
  ''' store of all modification that is associated to this account; :type: list of Modification objects'''
  balance = 0.0
  ''' balance of this account inf HUF; :type: float'''

  def __init__(self, acc_name, note):
    # create the first modification
    first_mod = Modification()
    first_mod.change = 0.0
    first_mod.reason = 'init'
    first_mod.time_stamp = None
    first_mod.modification_type = TransactionTypes.init
    first_mod.note = note

    # init the account
    self.name = acc_name
    self.note = note
    self.doModification(first_mod)
    return

  def doModification(self, mod):
    # check the field types
    assert (type(mod.change) == float) or (type(mod.change) == int), "[%s account] The content of modification's name field is not float or int"%self.name
    assert type(mod.reason) == str, "[%s account] The content of reason field in the modification is not string"%self.name
    assert type(mod.time_stamp) == datetime, "[%s account] The value in the time_stamp field of the modification is not a datetime format"%self.name
    assert type(mod.modification_type) == TransactionTypes, "[%s account] The value in the modification_type field of the modification is not in valid format"%self.name
    assert type(mod.note) == str, "[%s account] The value in the note field is not a string"%self.name
    # append the modification

    self.modification_list.append(mod)
    # update balance
    self.balance += mod.change
    return

  def getBalance(self):
    return self.balance

  def getNthTransaction(self, id_of_transaction):
    assert id_of_transaction >= len(self.modification_list)
    return self.modification_list[id_of_transaction]

  def getLastTransaction(self):
    return self.modification_list[len(self.modification_list) - 1]



