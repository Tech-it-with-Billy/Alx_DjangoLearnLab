# Permissions & Groups Setup

## Custom Permissions
The `Book` model defines the following custom permissions:
- `can_view`: Can view books
- `can_create`: Can create new books
- `can_edit`: Can edit existing books
- `can_delete`: Can delete books

## Groups
- **Viewers** - Assigned `can_view`
- **Editors** - Assigned `can_view`, `can_create`, `can_edit`
- **Admins** - Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`)

## Usage in Views
Permissions are enforced using `@permission_required`:
- `book_list` - Requires `can_view`
- `book_create` - Requires `can_create`
- `book_edit` - Requires `can_edit`
- `book_delete` - Requires `can_delete`

## Testing
1. Create users in Django Admin.
2. Assign them to `Viewers`, `Editors`, or `Admins`.
3. Log in and test each view.
