
variable "name" {
  type = string
  default = ""
}

variable "location" {
  type    = string
  default = ""
}

variable "resource_group_name" {
  type    = string
  default = ""
}

variable "sku" {
  type    = string
  default = ""
}

variable "retention_in_days" {
  type    = number
  default = 30
}
