resource "azurerm_role_definition" "main" {
  name        = local.role_name
  scope       = local.role_scope
  description = "This is a custom role created via Terraform"

  permissions {
    actions     = local.actions
    not_actions = local.no_actions
  }

  assignable_scopes = local.assignable_scopes
}