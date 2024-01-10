variable "name" {
  type = string
}

variable "key_permissions" {
  type = list(string)
  default = null
}

variable "secret_permissions" {
  type = list(string)
  default = null
}

variable "resource_group_name" {
  type = string
  description = "Name of resource group to deploy resources in."
}

variable "key_vault_name" {
  type = string
  description = "Name of the key_vault"
}

variable "object_id" {
  type = string
  description = "principal object id"
}
