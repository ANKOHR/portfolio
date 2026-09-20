import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Henry Williams — Software / Applied AI Engineer",
  description:
    "Henry Williams builds reliable AI, backend and automation systems with validation, auditability, human review and measurable evidence.",
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
  openGraph: {
    title: "Henry Williams — Software / Applied AI Engineer",
    description: "Reliable AI, backend and automation systems built around evidence.",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
