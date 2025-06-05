"use client";

import { Users, LibraryBig } from "lucide-react";

const icons = {
  LibraryBig,
  Users,
} as const;

type IconName = keyof typeof icons;

interface IconProps {
  name: IconName;
  className?: string;
}

export function Icon({ name, className }: IconProps) {
  const IconComponent = icons[name];
  return <IconComponent className={className} />;
} 