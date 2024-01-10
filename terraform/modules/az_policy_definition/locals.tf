locals {
  
  category = var.policy_category
  version = var.policy_version
  mode = var.policy_mode

  policy_name = var.policy_name
  display_name = var.display_name
  description = var.policy_description
  metadata = var.policy_metadata
  parameters = var.policy_parameters
  policy_rule = var.policy_rule
}