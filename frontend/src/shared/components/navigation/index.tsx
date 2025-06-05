"use client";

import Sidebar from "../sidebar";
import { Icon } from "./icon";
import { ComponentProps } from "react";

type IconName = "LibraryBig" | "Users";

interface Route {
  href: string;
  icon: IconName;
  label: string;
}

export default function Navigation() {
  const routes: Route[] = [
    {
      href: "/books",
      icon: "LibraryBig",
      label: "Books",
    },
    {
      href: "/authors",
      icon: "Users",
      label: "Authors",
    },
  ];

  return <Sidebar routes={routes.map(route => ({
    ...route,
    icon: (props: Omit<ComponentProps<typeof Icon>, 'name'>) => <Icon name={route.icon} {...props} />
  }))} />;
} 