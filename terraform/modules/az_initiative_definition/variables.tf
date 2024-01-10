variable initiative_name {
  type        = string
  description = "Policy initiative name. Changing this forces a new resource to be created"

  validation {
    condition     = length(var.initiative_name) <= 64
    error_message = "Initiative names have a maximum 64 character limit."
  }
}

variable initiative_display_name {
  type        = string
  description = "Policy initiative display name"
  default = ""
}

variable initiative_description {
  type        = string
  description = "Policy initiative description"
  default     = ""
}

variable policy_definition_id {
  type        = string
  default     = null
}

variable initiative_category {
  type        = string
  description = "The category of the initiative"
  default     = "General"
}

variable parameter_values {
  type        = any
  default     = null
}

variable parameters {
  type        = any
  default     = null
}

variable metadata {
  type        = any
  default     = null
}

