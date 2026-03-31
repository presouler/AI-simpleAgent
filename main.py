from openrouter import OpenRouter
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

with OpenRouter(
    # api_key=os.getenv("OPENROUTER_API_KEY")
    api_key,
) as client:
    agentmd = open("Agent.md","r").read()
    webSkillmd = open('webSkill.md').read()
    openwebmd = open('openweb.md').read()
    message = [{"role": 'system', "content": agentmd + webSkillmd + openwebmd}]
    while True:
      userInput = input("Message: ")
      message.append({"role": "user", "content": userInput})

      print("\n------ Agent Looping ------")

      while True:
        response = client.chat.send(
            model="minimax/minimax-m2",
            messages = message,
            max_tokens=500
        )
        reply = response.choices[0].message.content
        message.append({"role": "assistant", "content": reply})
        print(f"[AI] {reply}")
        if reply.strip().startswith('Done'):
           print("\n----- Agent Loop Ended ------")
           print(f"[AI] {reply.strip().split('Done')[1].strip()}")
           break
        if "Command:" not in reply:
          print("[Error] No command found")
          break
        command = reply.split("Command:", 1)[1].strip()

        command_result = os.popen(command).read()

        content = f"Execution complete: {command_result}"
        print(f"[Agent] {content}")
        message.append({"role": "user", "content": content})
