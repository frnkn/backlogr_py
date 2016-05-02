# Specs Backlogr

## Breakdown of Backlog items

"As a pm I'd like to break down backlog items by creating new backlog items and updating details of acceptance criterias, so that backlog items can get smaller."

**Acceptance Criteria**

* User clicks on breakdown button from item in list view
* Modal opens
* User enters backlog item data
* User saves
* backlog item keeps a reference to its parent
* backlog item is addded to the list

**Technical Spec**

* Add a field that acts a reference
* It's called parent_uuid
* It's optional, can be blank
* If break down happens it holds th uuid of the parent uuid
* The parents uuid is passed as url to the break down view

## Archiviving a card

"As a product manager I'd like to archive a backlog item, so that I does not occur in the listing, but in its own lising."

**Acceptance Criteria**
* User clicks on button "Archive"
* The Card gets invisible in the UI using an animation
* The backlog item get s the state is_archive = True

**Technical Spec**
* Add a field is_archive as boolean field
* default=True
* Archiving a list needs an update ajax view --> TODO

## Tagging a backlog item
"As a pm I'd like to give a backlog item tags, so that I can categorize an item."
