export function Footer() {
    return (
        <div className="py-4 gap-4 items-center justify-center absolute bottom-0 left-1/2 transform -translate-x-1/2">
        <a href="https://github.com/Jonsman" target="_blank" className="flex text-xs gap-2">
        <img
          src="/GitHub_Invertocat_Light.svg"
          alt="GitHub"
          className="h-5 w-5 dark:hidden"
        />
        <img
          src="/GitHub_Invertocat_Dark.svg"
          alt="GitHub"
          className="h-5 w-5 hidden dark:block"
        />
        by Jonsman
        </a>
      </div>
    )
}