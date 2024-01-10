resource "azurerm_role_assignment" "main" {
  scope              = local.role_assignment_scope
  role_definition_id = azurerm_role_definition.main.role_definition_resource_id
  principal_id       = local.principal_id
}

resource "azurerm_role_definition" "main" {
  name        = local.role_name
  scope       = local.role_scope
  description = "This is a custom role created via Terraform"

  permissions {
    actions     = local.actions
    not_actions = local.no_actions
    data_actions = local.data_actions
    not_data_actions = local.not_data_actions
  }

  assignable_scopes = local.assignable_scopes
}

data "azurerm_client_config" "current" {
}