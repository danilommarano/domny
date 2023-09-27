class XMLTag:

    def __init__(self, tag, *args, **kwargs) -> str:
        """Construct a representation of a XML tag

        Args:
            tag (str): Tag name
        """
        empty_tags = (
            'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 
            'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr'
        )
        self.__tag = tag
        self.__is_empty = tag in empty_tags

        self.attributes = {}
        self.childrens = []
        for arg in args:
            if type(arg) is str:
                setattr(self, arg, True)
                self.attributes[arg] = True
            elif type(arg) is type(self):
                self.childrens.append(arg)
                
        for key, value in kwargs.items():
            setattr(self, key, value)
            key = key[1:] if key.startswith('_') else key
            key = key.replace('_', '-')
            self.attributes[key] = value


    def __len__(self):
        return len(self.childrens)


    def __getitem__(self, key):
        children = self.childrens[key]
        return children
    

    def __setitem__(self, key, val):
        self.childrens[key] = val


    def __repr__(self):
        return self.render()


    def __str__(self):
        return self.render()
    
    
    def add(self, *args):
        self.childrens += args
        return self

    
    def render(self):
        attributes_as_string = ' '.join([
            key if value is True else f'{key}={value!r}'
            for key, value in self.attributes.items()
        ])

        if self.__is_empty:
            xml_tag = f"<{self.__tag} {attributes_as_string} />"
        else:
            xml_tag = (
                f"<{self.__tag} {attributes_as_string}>"
                    f"{''.join([str(child) for child in self.childrens])}"
                f"</{self.__tag}>"
            )

        return xml_tag
    