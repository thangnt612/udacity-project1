# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.
 App Services:
     - Analyze costs: can manage cost all app service use for the app
     - Scalability : 
                + Vertical : easily  increase or decrease amount of vCPUs or RAM.
                + Horizontal : increase instance of App Service is running
     - Availability : Can be enabled many regions
     - Workflow : They can create App services very quicky without installing
    
VM :
     - Analyze costs: They are more expensive
     - Scalability : Multiple types to choose from, such as compute or memory-optimized VMs, along with varying amounts of CPU, RAM, and storage
     - Availability : Multiple VMs can be grouped to provide high availability
     - Workflow : They can be more time consuming for the developer than other compute options

I choose AppService for deploying the app.
The reason:
    - I can manage the cost every app servvices when a deploy the app.
    - I don't need control OS or install software on the server.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

if the app need  for dedicated servers for security reasons. Developer can manually manage manually. I thinks I will choose Virtual Machines.