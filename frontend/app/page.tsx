import { Task } from "@/features/tasks/definitions";
import TaskCard from "@/features/tasks/ui/task-card";
import { apiClient } from "@/utils/api-client";

export default async function Home() {
  const tasks = await apiClient.get("/api/tasks")
  const data = tasks.data as Task[]
  console.log(data[0].id)

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Obcaecati distinctio omnis in laboriosam! Commodi dicta dolorum voluptas odit, corporis nihil rerum vero officiis eos ex? Iusto ab vero dolores sunt!
        </p>
        <div>
          {data.map(task => (
            <TaskCard task={task} key={task.id} />
          ))}
        </div>
      </div>
    </div>
  );
}
