"use client";

import { useState } from "react";
import Link from "next/link";
import { Button } from "../ui/button";
import { Sheet, SheetContent, SheetTrigger, SheetTitle } from "../ui/sheet";
import { MenuIcon, Users, LibraryBig } from "lucide-react";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "../ui/tooltip";

export default function Sidebar() {
  const routes = [
    {
      href: "/books",
      icon: LibraryBig,
      label: "Books",
    },
    {
      href: "/authors",
      icon: Users,
      label: "Authors",
    },
  ];

  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="flex w-full flex-col bg-muted/40">
      <aside className="fixed inset-y-0 left-0 z-10 hidden w-14 border-r bg-background sm:flex">
        <nav className="flex flex-col items-center gap-4 px-2 py-5">
          {routes.map((route) => (
            <TooltipProvider key={route.href}>
              <Tooltip>
                <TooltipTrigger asChild>
                  <Link 
                    href={route.href}
                    className="flex items-center gap-4 px-2.5 text-muted-foreground hover:text-foreground"
                  >
                    <route.icon className="h-4 w-5 transition-all" />
                    <span className="sr-only">{route.label}</span>
                  </Link>
                </TooltipTrigger>
                <TooltipContent side="right">{route.label}</TooltipContent>
              </Tooltip>
            </TooltipProvider>
          ))}
        </nav>
      </aside>
      <div className="sm:hidden flex flex-col sm:gap-4 sm:py-4 sm:pl-14">
        <header className="sticky top-0 z-30 flex h-14 items-center px-4 border-b bg-background sm:h-auto sm:border-0 sm:bg-transparent sm:px-6">
          <Sheet open={isOpen} onOpenChange={setIsOpen}>
            <SheetTrigger asChild>
              <Button variant="outline" size="icon" className="sm:hidden">
                <span className="sr-only">Open/Close Sidebar</span>
                <MenuIcon className="h-4 w-4" />
              </Button>
            </SheetTrigger>

            <SheetContent side="left" className="sm:max-w-x">
              <SheetTitle className="sr-only">Navigation Menu</SheetTitle>
              <nav className="grid gap-6 text-lg font-medium">
                {routes.map((route) => (
                  <Link 
                    key={route.href}
                    href={route.href}
                    onClick={() => setIsOpen(false)}
                    className="flex items-center gap-4 px-2.5 text-muted-foreground hover:text-foreground"
                  >
                    <route.icon className="h-4 w-5 transition-all" />
                    {route.label}
                  </Link>
                ))}
              </nav>
            </SheetContent>
          </Sheet>
          <h2 className="text-lg font-semibold pl-2">Menu</h2>
        </header>
      </div>
    </div>
  );
}
