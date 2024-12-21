import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card";
import { Task } from "../definitions";

function TaskCard({ task }: { task: Task }) {
  return (
    <Card className="max-w-[400px] bg-slate-900">
      <CardHeader>{task.title}</CardHeader>
      <CardContent>{task.content}</CardContent>
      <CardFooter>
        <small className="text-right">{task.created_at}</small>
      </CardFooter>
    </Card>);
}

export default TaskCard;