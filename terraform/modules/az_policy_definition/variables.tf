variable management_group_id {
  type        = string
  description = "The management group scope at which the policy will be defined. Defaults to current Subscription if omitted. Changing this forces a new resource to be created."
  default     = null
}

variable policy_name {
  type        = string
  description = "Name to be used for this policy."
  default     = ""
}

variable display_name {
  type        = string
  description = "Display Name to be used for this policy"
  default     = ""
}

variable policy_description {
  type        = string
  description = "Policy definition description"
  default     = ""
}

variable policy_mode {
  type        = string
  description = "The policy mode that allows you to specify which resource types will be evaluated, defaults to All. Possible values are All and Indexed"
  default     = null
}

variable policy_category {
  type        = string
  description = "The category of the policy"
  default     = null
}

variable policy_version {
  type        = string
  description = "The version for this policy, if different from the one stored in the definition metadata, defaults to 1.0.0"
  default     = null
}

variable policy_rule {
  type        = any
  description = "The policy rule for the policy definition. "
  default     = null
}

variable policy_parameters {
  type        = any
  description = "Parameters for the policy definition. "
  default     = null
}

variable policy_metadata {
  type        = any
  description = "The metadata for the policy definition."
  default     = null
}


