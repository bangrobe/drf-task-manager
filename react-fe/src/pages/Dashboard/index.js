import React from "react";
import TasksCompletion from "./TasksCompletion";
import TasksByCategory from "./TasksByCategory";
const Dashboard = () => {
  return (
    <div>
      <TasksCompletion />
      <TasksByCategory />
    </div>
  );
};

export default Dashboard;
