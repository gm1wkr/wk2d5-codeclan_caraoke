# CodeClan_Caraoke 

## MVP
Guests can be checked into a room

Guests can be checked out of a room

Songs can be added to the rooms playlist

## Extensions
If a room is full the guest is declined entry.

Guests have a wallet and rooms have an entry fee. 

The Guest wallet is checked for funds before being added to the rooms till.  

## Advanced Extensions
started but not completed.

If a guests favourite song is present in the rooms playlist then the guest can cheer loudly and "Gie It Laldy".

A bar_tab class has been started.  The bar_tab will track the running_total of money owed per guest.  

A Drinks class has been created. Drinks have a name, stock level and price.  Helper methods have been created to 
track drinks taken out of inventory and to return the price and stock level for other classes to use.

## Next Steps
Given more time the following steps would be taken.

1. The guest would be offered an alernative room if there is no space left in their choosen room.
2. The bar tab would be made functional.  A guest in a room would be able to order a drink on tab.  The BarTab class would be called from Room when a guest orders a drink or when the guest leaves a room and needs to settle the tab.
3. Room Fee and Bar Tab (would, if completed) have some duplicted functionality such as checking to see if the guest has sufficient funds.  Refactoring would help keep the app DRY.
4. Some confussion about responsibilties remain, would the room be in ultimate charge of the Bar Tab?
5. Class diagram would be fully updated to reflect refactoring.