class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        new_list = []
        for email in emails:
            name, domain = email.split('@')
            name = name.replace('.', '')
            name_before_plus = name.split('+')[0]
            processed_email = name_before_plus + '@' + domain
            print(processed_email)
            if processed_email not in new_list:
                new_list.append(processed_email)
                
        return len(new_list)
    