resource "azurerm_key_vault_access_policy" "main" {
  key_vault_id = data.azurerm_key_vault.main.id
  tenant_id = data.azurerm_key_vault.main.tenant_id
  object_id = var.object_id
  secret_permissions      = var.secret_permissions
  key_permissions         = var.key_permissions
}

data "azurerm_key_vault" "main" {
  name                = var.key_vault_name
  resource_group_name = var.resource_group_name
}

data "azurerm_client_config" "current" {}