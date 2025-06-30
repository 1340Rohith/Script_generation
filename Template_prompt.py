Master_prompt = "Primary_Instruction: {master_primary_instruction}\n" \
               "Message: {message}\n" \
               "Secondary_instruction: {master_secondary_instruction}\n" \
               "Changes: {changes}\n" \
               "History of Completed changes: {previous_changes_master}\n"

Sub_agent_prompt = "Primary_Instruction: {sub_primary_instruction}\n" \
               "Secondary_instruction: {sub_secondary_instruction}\n" \
               "Previous_Story: {history_story}\n"\
               "Message: {message_sub}\n" \
               "Previous_Changes: {previous_changes_sub}\n"  

#for master agent the history is the previous completed changes
#for the sub agents the history is the previous story written by the master agent


changes = "Logical_Agent: {logical_agent}\n" \
         "Creativity_Agent: {creativity_agent}\n" \
         "user_changes: {user_changes}\n" \
         
#master_primary_instruction = "You are a Skillfull storywriter who will Write a story based on the given message in 3 acts"
#master_secondary_instruction = "if Changes are provided, you must incorporate them into the story. "

