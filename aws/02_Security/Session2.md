# IAM (Identity and Access Management)
## How IAM Works?
IAM provides the infrastructure necessary to control authentication and authorization for your account.

## Key Terms
- Resources <br> The user, group, role, policy, and identity provider objects that are stored in IAM. As with other AWS services, you can add, edit, and remove resources from IAM.
- Identities <br> The IAM resource objects that are used to identify and group. You can attach a policy to an IAM identity. These include users, groups, and roles.
- Entities <br> The IAM resource objects that AWS uses for authentication. These include users and roles. Roles can be assumed by IAM users and roles in your or another account. They can also be assumed by users federated through a web identity or SAML.
- Principals <br> A person or application that uses the AWS account root user, an IAM user, or an IAM role to sign in and make requests to AWS.
Security and IAM (Identity and Access Management)
- ## Users
- ## Groups
- ## Policies
- ## Roles

## Command used during the session
```
aws iam list-users
aws iam list-users --output text
aws iam list-users --output table
aws iam list-users --output json  --query 'Users[*].[UserName,Arn,CreateDate,PasswordLastUsed,UserId]'
aws iam update-user --user awsdemo --new-user-name awssession

```
## FAQ
- What is a root user in AWS? <br>When the user first create an AWS account, user begin with a single sign-in identity that has complete access to all AWS services and resources in the account. This identity is called the AWS account _root user_ and is accessed by signing in with the email address and password that user used to create the account. _Root user credentials and use them to perform only a few account and service management tasks._

[AWS IAM Introduction Video](https://www.aws.training/Details/Video?id=16448)

**Useful links** <br>
- [AWS CLI Configurations](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
- [AWS CLI Usage](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output.html)