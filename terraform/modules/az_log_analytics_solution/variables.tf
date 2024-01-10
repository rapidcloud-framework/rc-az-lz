
variable "solution_name" {
  type = string
  default = ""
}

variable "location" {
  type    = string
  default = ""
}

variable resource_group_name {
  type        = string
  default = null
}

variable workspace_resource_id {
  type        = string
  default = ""
}

variable workspace_name {
  type        = string
  default = null
}

variable product {
  type        = string
  default = "ContainerInsights"
}

variable publisher {
  type        = string
  default = "Publisher"
}

