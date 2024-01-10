data "azurerm_subscription" "current" {
}

resource "azurerm_management_group" "main" { 
  name = local.management_group_name
  parent_management_group_id = data.azurerm_management_group.main.id
}

resource "azurerm_management_group_policy_assignment" "main" {
  name                 = var.policy_assignment_name
  policy_definition_id = var.policy_definition_id
  management_group_id  = azurerm_management_group.main.id
}

data "azurerm_management_group" "main" {
  name = local.parent_management_group_id
}


