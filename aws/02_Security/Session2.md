# Security and IAM (Identity and Access Management)
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


**Useful links** <br>
- [AWS CLI Configurations](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
- [AWS CLI Usage](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output.html)